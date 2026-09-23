using Microsoft.EntityFrameworkCore;
using System.Runtime.InteropServices;

namespace TretiProjekt
{
    class Student
    {
        public int StudentID { get; set; } //primarni klic
        public required string Jmeno { get; set; }
        public int SkupinaID { get; set; } //cizi klic
        public Skupina? Skupina { get; set; }
    }

    class Skupina
    {
        public int SkupinaID { get; set; }
        public required string Nazev { get; set; }
        public List<Student> Studenti { get; set; }
    }

    class SkolaContext(DbContextOptions<SkolaContext> options) : DbContext(options)
    {
        public DbSet<Student> Studenti { get; set; }
        public DbSet<Skupina> Skupiny { get; set; }

    }
    internal class Program
    {
        public static SkolaContext CreateContext()
        {
            var options = new DbContextOptionsBuilder<SkolaContext>()
                .UseSqlite("DataSource=skola.db")
                .LogTo(Console.WriteLine, Microsoft.Extensions.Logging.LogLevel.Information)
                .EnableSensitiveDataLogging(true)
                .Options;

            return new SkolaContext(options);
        }

        public static async Task Seed()
        {
            await using SkolaContext context = CreateContext();

            await context.Database.EnsureDeletedAsync();
            await context.Database.EnsureCreatedAsync();

            Skupina skupina1 = new() { SkupinaID = 1, Nazev = "SWI1" };
            Skupina skupina2 = new() { SkupinaID = 2, Nazev = "SWI2" };

            Student student1 = new() { StudentID = 1, Jmeno = "Martin", SkupinaID = 1 };
            Student student2 = new() { StudentID = 2, Jmeno = "Roman", SkupinaID = 2 };
            Student student3 = new() { StudentID = 2, Jmeno = "¨Petr", SkupinaID = 2 };

            await context.Skupiny.AddRangeAsync(skupina1, skupina1);
            await context.Studenti.AddRangeAsync(student1, student2, student3);


        }

        public static async Task VypisSkupiny()
        {
            await using SkolaContext context = CreateContext();

            Console.WriteLine("Skupiny:");

            foreach (Skupina skupina in await context.Skupiny.Include(sk => sk.Studenti).ToListAsync())
            {
                Console.WriteLine($"{skupina.SkupinaID} {skupina.Nazev}");

                if (skupina.Studenti is not null)
                {
                    foreach (Student student in skupina.Studenti)
                    {
                        Console.WriteLine($"    {student.Jmeno}");
                    }
                }
            }

        class Karta
        {
            public int KartaId { get; set; }
            public decimal Zustatek { get; set; }
            public int StudentID { get; set; }
            public Student? Student { get; set; }


        static async Task Main(string[] args)
        {
            await Seed();
        }
    }
}