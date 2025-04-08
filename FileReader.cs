using System;
using System.IO;

class FileReader
{
    static void Main(string[] args)
    {
        Console.WriteLine("Enter the file path:");
        string filePath = Console.ReadLine();

        try
        {
            string fileContent = File.ReadAllText(filePath);
            Console.WriteLine("File Content:");
            Console.WriteLine(fileContent);
        }
        catch (FileNotFoundException)
        {
            Console.WriteLine("Error: File not found.");
        }
        catch (UnauthorizedAccessException)
        {
            Console.WriteLine("Error: Access to the file is denied.");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
    }
}
