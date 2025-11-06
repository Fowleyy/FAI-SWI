namespace DOTNET.Models
{
    public enum SharePermission
    {
        Read,
        Edit,
        Owner
    }

    public class CalendarShare
    {
        public int Id { get; set; }
        public int CalendarId { get; set; }
        public int SharedWithUserId { get; set; }
        public SharePermission Permission { get; set; }

        public Calendar Calendar { get; set; }
        public User SharedWithUser { get; set; }
    }
}
