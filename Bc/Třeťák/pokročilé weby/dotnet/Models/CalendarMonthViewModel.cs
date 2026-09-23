using System.Collections.Generic;

namespace DOTNET.Models
{
    public class CalendarMonthViewModel
    {
        public int Year { get; set; }
        public int Month { get; set; }
        public string MonthName { get; set; }
        public int DaysInMonth { get; set; }
        public int FirstDayOfWeek { get; set; } // Po = 1, Ne = 7
        public List<CalendarEvent> Events { get; set; }
    }
}