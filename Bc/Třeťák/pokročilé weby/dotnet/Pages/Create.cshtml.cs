using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using DOTNET.Data;
using DOTNET.Models;

namespace DOTNET.Pages
{
    public class CreateModel : PageModel
    {
        private readonly EventContext _context;

        public CreateModel(EventContext context)
        {
            _context = context;
        }

        [BindProperty]
        public Event Event { get; set; } = new Event();

        public void OnGet()
        {
            var now = DateTime.Now;
            var nextHour = now.Minute == 0 && now.Second == 0 ? now : new DateTime(now.Year, now.Month, now.Day, now.Hour + 1, 0, 0);
            Event.StartTime = nextHour;
            Event.EndTime = nextHour.AddHours(1);
        }

        public IActionResult OnPost()
        {
            if (Event.StartTime.Minute != 0 || Event.EndTime.Minute != 0)
            {
                ModelState.AddModelError("", "Čas musí být zadán pouze na celé hodiny (minuty musí být 00).");
                return Page();
            }

            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.Events.Add(Event);
            _context.SaveChanges();

            return RedirectToPage("./Index");
        }
    }
}
