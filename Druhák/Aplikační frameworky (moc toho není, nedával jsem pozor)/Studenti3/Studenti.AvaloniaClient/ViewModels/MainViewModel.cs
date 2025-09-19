using CommunityToolkit.Mvvm.ComponentModel;
using Studenti.AvaloniaClient.Services;
using System.Linq;
using System.Net.Http.Json;
using System.Text.Json;
using System.Threading.Tasks;

namespace Studenti.AvaloniaClient.ViewModels;

public partial class MainViewModel : ViewModelBase
{
    [ObservableProperty]
    private Student[]? students;

    [ObservableProperty]
    private Student? selectedStudent;

    private readonly SaveDialogService saveDialog;

    public MainViewModel(SaveDialogService saveDialog)
    {
        Task.Run(LoadStudentAsync);
        this.saveDialog = saveDialog;
    }

    private async Task LoadStudentAsync()
    {
        Students = await App.sharedClient.GetFromJsonAsync<Student[]>("/students"); 

        SelectedStudent = Students?.FirstOrDefault();
    }

    public async Task Save()
    {
        if (SelectedStudent is not null)
        {
            await App.sharedClient.PutAsJsonAsync($"/students/{SelectedStudent.StudentId}", SelectedStudent);
        }
    }

    public async Task Export()
    {
        if(Students is not null)
        {
            string json = JsonSerializer.Serialize(Students);
            await saveDialog.SaveDialogAsync(json);
        }
    }
}
