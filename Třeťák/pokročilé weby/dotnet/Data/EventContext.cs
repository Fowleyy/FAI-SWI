using Microsoft.EntityFrameworkCore;
using DOTNET.Models;

namespace DOTNET.Data
{
    public class EventContext : DbContext
    {
        public EventContext(DbContextOptions<EventContext> options)
            : base(options)
        {
        }
        public DbSet<Event> Events { get; set; }
    }
}
