using Contracts;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;

namespace CredibilityModel.Tests
{
    [TestClass]
    public class CredibilityIntegrationTests
    {
        [TestMethod]
        public void CalculateProbability_Mammography_10000Testees_CredibilityIs0Point08()
        {
            var medicalTestData = new MedicalTestData
            {
                Test = "Mammography",
                Diagnosis = "Breast Cancer",
                Prevalence = 0.01,
                Sensitivity = 0.8,
                Specificity = 0.904
            };

            var credibility = Credibility.CalculateCredibility(testees: 10000, medicalTestData);

            Assert.AreEqual(0.08, Math.Round(credibility, 2));
        }
    }
}