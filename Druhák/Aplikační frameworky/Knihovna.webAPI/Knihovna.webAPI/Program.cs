using Microsoft.AspNetCore.Http.HttpResults;
using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

namespace PuchovSK
{
    public class Kniha
    {
        public int KnihaId { get; set; }
        public required string Nazev { get; set; }
    }

    public class KnihovnaContext(DbContextOptions<KnihovnaContext> options) : DbContext(options)
    {
        public DbSet<Kniha> Knihy { get; set; }
    }
    public class Program
    {
        public static void Main(string[] args)
        {
            var builder = WebApplication.CreateBuilder(args);
            var app = builder.Build();

            app.MapGet("/knihy", WebApi1.VratVsechnyKnihy);

            app.MapPost("/knihy", WebApi1.PridejKnihu);

            app.Run();
        }


        public static class WebApi1
        {
            public static async Task<Ok<Kniha[]>> VratVsechnyKnihy(KnihovnaContext context)
            {
                var knihy = await context.Knihy.ToArrayAsync();
                return TypedResults.Ok(knihy);
            }
            public static async Task<Created<Kniha>> PridejKnihu(KnihovnaContext context, Kniha book)
            {
                context.Knihy.Add(book);
                await context.SaveChangesAsync();
                return TypedResults.Created($"knihy/{book.KnihaId}", book);
            }
        }
    }
}

