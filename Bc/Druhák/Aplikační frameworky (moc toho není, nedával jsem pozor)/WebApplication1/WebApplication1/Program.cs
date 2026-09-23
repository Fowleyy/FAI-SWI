using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.EntityFrameworkCore;

namespace WebApplication1
{
    class Student
    {
        public int StudentId { get; set; }
        public required string Jmeno { get; set; }
        public required bool Studuje { get; set; }
    }

    class StudentContext(DbContextOptions<StudentContext> options) : DbContext(options)
    {
        public DbSet<Student> Studenti { get; set; }
    }

    internal class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);

            string? connectionString = builder.Configuration.GetConnectionString("Studenti");
            builder.Services.AddDbContext<StudentContext>(options => options.UseSqlite(connectionString));

            var app = builder.Build();

            app.MapGet("/seed", Seed);
            app.MapGet("/students", GetAllStudents);
            app.MapGet("/studujici", GetStudujiciStudents);

            app.Run();
        }

        public static async Task<Created> Seed(StudentContext context)
        {
            await context.Database.EnsureDeletedAsync();
            await context.Database.EnsureCreatedAsync();

            Student student1 = new() { StudentId = 1, Jmeno = "Petr", Studuje = true };
            Student student2 = new() { StudentId = 2, Jmeno = "Josef", Studuje = false };
            Student student3 = new() { StudentId = 3, Jmeno = "Lojza", Studuje = true };

            await context.Studenti.AddRangeAsync(student1, student2, student3);
            await context.SaveChangesAsync();

            return TypedResults.Created();
        }

        public static async Task<Ok<Student[]>> GetAllStudents(StudentContext context)
        {
            Student[] studenti = await context.Studenti.ToArrayAsync();
            return TypedResults.Ok(studenti);
        }

        public static async Task<Ok<Student[]>> GetStudujiciStudents(StudentContext context)
        {
            Student[] studenti = await context.Studenti.Where(s => s.Studuje).ToArrayAsync();
            return TypedResults.Ok(studenti);
        }
    }
}