namespace DOTNET.Models
{
    public class Calendar
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public int OwnerId { get; set; }

        public User Owner { get; set; }
        public ICollection<Event> Events { get; set; }
        public ICollection<CalendarShare> Shares { get; set; }
    }
}
