namespace DOTNET.Models
{
    public class User
    {
        public int Id { get; set; }
        public string UserName { get; set; }
        public string Email { get; set; }
        public string PasswordHash { get; set; }

        public ICollection<Calendar> Calendars { get; set; }
        public ICollection<CalendarShare> CalendarShares { get; set; }
    }
}
