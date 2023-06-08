namespace CommandLine
{
    public class CommandLine
    {
        public string ReadDiagnosisOrTest()
        {
            Console.WriteLine("Enter diagnosis or test: ");
            return Console.ReadLine();
        }

        public int ReadTesteesCount()
        {
            Console.WriteLine("Enter number of testees: ");
            return int.Parse(Console.ReadLine());
        }

        public void WaitForExit()
        {
            Console.WriteLine("Press any key to exit");
            Console.ReadKey();
        }

        public void WriteResult(double credibility)
        {
            Console.WriteLine($"Credibility: {Math.Round(credibility, 2)}");
        }
    }
}