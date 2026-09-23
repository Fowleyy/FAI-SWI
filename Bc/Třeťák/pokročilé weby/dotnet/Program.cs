using DOTNET.Models;
using Microsoft.EntityFrameworkCore;
using DOTNET.Data;


var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<EventContext>(options =>
    options.UseSqlite("Data Source=events.db"));
    
builder.Services.AddDbContext<CalendarDbContext>(options =>
    options.UseSqlite(builder.Configuration.GetConnectionString("DefaultConnection")));

builder.Services.AddRazorPages();

var app = builder.Build();

app.UseStaticFiles();
app.UseRouting();
app.MapRazorPages();
app.MapControllers();
app.Run();
