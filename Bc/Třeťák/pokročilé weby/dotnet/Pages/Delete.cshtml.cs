using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using DOTNET.Models;

namespace DOTNET.Pages
{
    public class DeleteModel : PageModel
    {
        [BindProperty]
        public Event Event { get; set; }

        public void OnGet(int id)
        {
        }

        public IActionResult OnPost()
        {
            return RedirectToPage("Index");
        }
    }
}
