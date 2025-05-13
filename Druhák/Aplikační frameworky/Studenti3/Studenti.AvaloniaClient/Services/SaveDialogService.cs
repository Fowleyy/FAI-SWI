using Avalonia.Controls;
using Avalonia.Platform.Storage;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Studenti.AvaloniaClient.Services
{
    public class SaveDialogService(TopLevel topLevel)
    {
        private readonly TopLevel topLevel = topLevel;
        public async Task SaveDialogAsync(string json)
        {
            var jsonFileType = new FilePickerFileType("JSON File")
            {
                Patterns = ["*.json"],
                MimeTypes = ["application/json"]
            };

            var options = new FilePickerSaveOptions
            {
                Title = "Save export file",
                DefaultExtension = "json",
                FileTypeChoices = [jsonFileType]
            };

            IStorageFile? file = await topLevel.StorageProvider.SaveFilePickerAsync(options);

            if (file is not null)
            {
                await using var stream = await file.OpenWriteAsync();

                using var streamWriter = new StreamWriter(stream);

                await streamWriter.WriteAsync(json);
            }
        }
    }
}
