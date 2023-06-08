// See https://aka.ms/new-console-template for more information
using CommandLine;
using CredibilityModel;
using TestDataProvider;

var testDataProvider = new TestDataProvider.TestDataProvider();
testDataProvider.LoadTestDataFile(args[0]);
var commandLine = new CommandLine.CommandLine();
string diagnosisOrTest = commandLine.ReadDiagnosisOrTest();
var medicalTestData = testDataProvider.GetTestData(diagnosisOrTest);
int testeesCount = commandLine.ReadTesteesCount();
var credibility = Credibility.CalculateCredibility(testeesCount, medicalTestData);
commandLine.WriteResult(credibility);
commandLine.WaitForExit();

