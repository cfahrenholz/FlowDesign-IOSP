using CredibilityModel;

namespace CredibilityModel.Tests
{
    [TestClass]
    public class CredibilityTests
    {
        [TestMethod]
        public void CalculateCredibility_80TruePositives_950FalsePositives_Returns0_08()
        {
            var credibility = Credibility.CalculateCredibility(truePositives: 80, falsePositives: 950);

            Assert.AreEqual(0.08, Math.Round(credibility, 2));
        }


    }
}