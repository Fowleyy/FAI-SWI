using DOTNET.Data;
using Microsoft.AspNetCore.Mvc;
using System.Globalization;
using System.Linq;

namespace DOTNET
{
    [ApiController]
    [Route("Calendar")]
    public class CalendarController : ControllerBase
    {
        private readonly EventContext _context;
        public CalendarController(EventContext context)
        {
            _context = context;
        }

        [HttpGet("GetMonth")]
        public IActionResult GetMonth(int year, int month)
        {
            var daysInMonth = DateTime.DaysInMonth(year, month);

            var events = _context.Events
                .Where(ev => ev.StartTime.Year == year && ev.StartTime.Month == month)
                .Select(ev => new
                {
                    title = ev.Title,
                    day = ev.StartTime.Day,
                    start = ev.StartTime.ToString("HH:mm"),
                    end = ev.EndTime.ToString("HH:mm")
                })
                .ToList();

            var monthName = new DateTime(year, month, 1)
                .ToString("MMMM", new CultureInfo("cs-CZ"));

            return Ok(new
            {
                year,
                month,
                monthName,
                daysInMonth,
                events
            });
        }
    }
}
