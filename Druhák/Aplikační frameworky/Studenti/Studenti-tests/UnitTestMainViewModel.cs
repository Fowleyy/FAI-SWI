using Studenti.AvaloniaClient.Services;
using Studenti.AvaloniaClient.ViewModels;
using System.Text.Json;
using System.Text.Json.Nodes;
using System.Threading.Tasks;

namespace Studenti_tests
{
    class MockStudentService : IStudentService
    {
        public Student[]? Studenti { get; } =
            [
            new Student() { StudentId = 1, Jmeno = "kokotko", Studuje = true},
            new Student() { StudentId = 2, Jmeno = "retarder", Studuje = true},
            new Student() { StudentId = 3, Jmeno = "Peta Happy", Studuje = false}
            ];
        public Task<Student[]?> GetAllStudentsAsync()
        {
            return Task.FromResult(Studenti);
        }

        public Task UpdateStudentAsync(Student student)
        {
            Student? studentToChange = Studenti?.FirstOrDefault(s => s.StudentId == student.StudentId);

            if(studentToChange is not null)
            {
                studentToChange.Jmeno = student.Jmeno;
                studentToChange.Studuje = student.Studuje;
            }
            return Task.CompletedTask;
        }
    }
    class FakeSaveDialogService : ISaveDialogService
    {
        public string? Json { get; private set; }
        public Task SaveAsync(string json)
        {
            Json = json;

            return Task.CompletedTask;
        }
    }
    public class UnitTestMainViewModel
    {
        [Fact]
        public async Task Test_ExportStudents_ShouldExportStudents()
        {
            MockStudentService studentService = new();
            FakeSaveDialogService dialogService = new();

            MainViewModel viewModel = new(studentService, dialogService);

            await viewModel.LoadStudentAsync();
            await viewModel.Export();

            string json = JsonSerializer.Serialize(studentService.Studenti);

            Assert.Equal(json , dialogService.Json);
        }

        [Fact]
        public async Task Test_SaveStudent_ShouldSaveStudent()
        {
            MockStudentService studentService = new();
            FakeSaveDialogService dialogService = new();

            MainViewModel viewModel = new(studentService, dialogService);

            await viewModel.LoadStudentAsync();
            Assert.NotNull(viewModel.Students);
            Assert.NotNull(viewModel.SelectedStudent);

            viewModel.SelectedStudent.Jmeno = "David";
            viewModel.SelectedStudent.Studuje = false;

            await viewModel.Save();

            Assert.NotNull(studentService.Studenti);

            Student updatedStudent = studentService.Studenti.First(s => s.StudentId == viewModel.SelectedStudent.StudentId);

            Assert.Equal("David", updatedStudent.Jmeno);
            Assert.False(updatedStudent.Studuje);
        }
    }
}
