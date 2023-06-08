using Contracts;
using System.Runtime.CompilerServices;

[assembly: InternalsVisibleTo("CredibilityModel.Tests")]

namespace CredibilityModel
{
    public static class Credibility
    {
        public static double CalculateCredibility(int testees, MedicalTestData testData)
        {
            var realPositives = GetRealPositives(testees, testData.Prevalence);
            var truePositives = GetTruePositives(realPositives, testData.Sensitivity);
            var realNegatives = GetRealNegatives(testees, realPositives);
            var trueNegatives = GetTrueNegatives(realNegatives, testData.Specificity);
            var falsePositives = GetFalsePositives(realNegatives, trueNegatives);

            return CalculateCredibility(truePositives, falsePositives);
        }

        private static double GetRealPositives(int testees, double prevalence)
        {
            return prevalence * testees;
        }

        private static double GetTruePositives(double realPositives, double sensitivity)
        {
            return sensitivity * realPositives;
        }

        private static double GetRealNegatives(int testees, double realPositives)
        {
            return testees - realPositives;
        }

        private static double GetTrueNegatives(double realNegatives, double specificity)
        {
            return realNegatives * specificity;
        }

        private static double GetFalsePositives(double realNegatives, double trueNegatives)
        {
            return realNegatives - trueNegatives;
        }

        internal static double CalculateCredibility(double truePositives, double falsePositives)
        {
            var credibility = truePositives / (truePositives + falsePositives);
            return credibility;
        }

    }
}