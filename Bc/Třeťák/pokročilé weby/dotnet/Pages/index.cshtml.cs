using System;
using System.Collections.Generic;
using System.Globalization;
using Microsoft.AspNetCore.Mvc.RazorPages;

namespace DOTNET
{
    public class IndexModel : PageModel
    {
        public int Year { get; set; }
        public int Month { get; set; }
        public int DaysInMonth { get; set; }
        public string MonthYearTitle { get; set; }
        public List<EventItem> Events { get; set; } = new List<EventItem>();

        // Nová property:
        public int? SelectedDay { get; set; }

        public void OnGet(int? year = null, int? month = null, int? selectedDay = null)
        {
            var dnes = DateTime.Today;
            Year = year ?? dnes.Year;
            Month = month ?? dnes.Month;
            DaysInMonth = DateTime.DaysInMonth(Year, Month);

            var monthName = CultureInfo.GetCultureInfo("cs-CZ")
                .DateTimeFormat.GetMonthName(Month);
            MonthYearTitle = char.ToUpper(monthName[0]) + monthName.Substring(1) + " " + Year;

            // Ukázkové události:
            Events = new List<EventItem>
            {
                new EventItem { Date = new DateTime(Year, Month, 5), Title = "Porada týmu" },
                new EventItem { Date = new DateTime(Year, Month, 12), Title = "Zubař" },
                new EventItem { Date = new DateTime(Year, Month, 22), Title = "Narozeniny kamaráda" }
            };

            SelectedDay = selectedDay;
        }

        public class EventItem
        {
            public DateTime Date { get; set; }
            public string Title { get; set; }
        }
    }
}