using Contracts;

namespace TestDataProvider
{
    public class TestDataProvider
    {
        private IEnumerable<MedicalTestData> _testDataEntries;

        public MedicalTestData GetTestData(string diagnosisOrTest)
        {
            return _testDataEntries
                .FirstOrDefault(e => e.Diagnosis == diagnosisOrTest || e.Test == diagnosisOrTest) ?? throw new NullReferenceException();
        }

        public IEnumerable<MedicalTestData> LoadTestDataFile(string filePath)
        {
            var fileContent = File.ReadAllText(filePath);
            _testDataEntries = Newtonsoft.Json.JsonConvert.DeserializeObject<IEnumerable<MedicalTestData>>(fileContent) ?? throw new NullReferenceException();
            return _testDataEntries;
        }
    }
}