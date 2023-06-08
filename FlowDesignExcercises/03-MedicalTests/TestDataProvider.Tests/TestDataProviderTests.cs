using TestDataProvider;
namespace TestDataProviderTests
{
    [TestClass]
    public class TestDataProviderTests
    {
        [TestMethod]
        public void LoadTestDataFile_AllEntriesLoaded()
        {
            var testee = new TestDataProvider.TestDataProvider();
            var entries = testee.LoadTestDataFile("03-MedicalTestsDB.json");

            Assert.AreEqual(3, entries.Count());
        }

        [TestMethod]
        public void GetTestData_ByDiagnoseBreastCancer_MammographyEntryReturned()
        {
            var testee = new TestDataProvider.TestDataProvider();
            testee.LoadTestDataFile("03-MedicalTestsDB.json");
            var mammographyEntry = testee.GetTestData("Breast Cancer");
            Assert.AreEqual("Mammography", mammographyEntry.Test);
            
        }
    }
}