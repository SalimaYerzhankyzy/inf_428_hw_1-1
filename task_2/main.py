import numpy as np
import unittest


# Function to generate random threat data
def generate_random_data(mean, variance, num_samples):
    return np.random.randint(max(mean - variance, 0), min(mean + variance + 1, 90), num_samples)


# Function to compute the department's average threat score
def compute_department_score(threat_scores):
    return np.mean(threat_scores)


# Function to compute the overall company's aggregated threat score
def compute_aggregated_threat_score(department_scores, department_importance):
    # Weighted average of department scores
    total_importance = sum(department_importance)
    weighted_sum = sum(score * importance for score, importance in zip(department_scores, department_importance))
    return weighted_sum / total_importance if total_importance > 0 else 0


# Functional test case using unittest
class TestCyberSecurity(unittest.TestCase):

    def setUp(self):
        # Setup basic department parameters for test cases
        self.departments = ['Engineering', 'Marketing', 'Finance', 'HR', 'Science']
        self.num_departments = len(self.departments)

    def test_case_1_no_outliers_same_importance(self):
        """ Case where all departments have no outliers, similar threat scores, and equal importance """
        department_importance = [3, 3, 3, 3, 3]  # Equal importance for all departments
        department_scores = []

        # Generate threat scores for each department
        for _ in range(self.num_departments):
            threat_scores = generate_random_data(mean=45, variance=10, num_samples=100)
            dept_score = compute_department_score(threat_scores)
            department_scores.append(dept_score)

        # Compute the aggregated threat score
        aggregated_score = compute_aggregated_threat_score(department_scores, department_importance)
        print(f"Aggregated Score: {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= 90, f"Aggregated score is out of range: {aggregated_score}")

    def test_case_2_high_importance_department(self):
        """ Case where one department has significantly higher importance than others """
        department_importance = [1, 1, 5, 1, 1]  # Finance has higher importance
        department_scores = []

        # Generate threat scores for each department
        for _ in range(self.num_departments):
            threat_scores = generate_random_data(mean=45, variance=10, num_samples=100)
            dept_score = compute_department_score(threat_scores)
            department_scores.append(dept_score)

        # Compute the aggregated threat score
        aggregated_score = compute_aggregated_threat_score(department_scores, department_importance)
        print(f"Aggregated Score with weighted Finance department: {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= 90, f"Aggregated score is out of range: {aggregated_score}")

    def test_case_3_varied_threat_scores_and_importance(self):
        """ Case where departments have varying importance and threat score distributions """
        department_importance = [5, 1, 3, 2, 4]  # Different importance for each department
        department_scores = []

        # Generate threat scores for each department with varying means and variances
        dept_params = [(50, 15), (30, 5), (60, 20), (40, 10), (55, 10)]
        for (mean, variance) in dept_params:
            threat_scores = generate_random_data(mean=mean, variance=variance, num_samples=100)
            dept_score = compute_department_score(threat_scores)
            department_scores.append(dept_score)

        # Compute the aggregated threat score
        aggregated_score = compute_aggregated_threat_score(department_scores, department_importance)
        print(f"Aggregated Score with varied importance and threat distribution: {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= 90, f"Aggregated score is out of range: {aggregated_score}")

    def test_case_4_extreme_outliers(self):
        """ Case where some departments have extreme outliers """
        department_importance = [3, 3, 3, 3, 3]  # Equal importance for all departments
        department_scores = []

        # Generate threat scores with extreme outliers for one department
        department_params = [
            (50, 10),  # Engineering
            (50, 10),  # Marketing
            (70, 50),  # Finance (extreme outliers)
            (50, 10),  # HR
            (50, 10)  # Science
        ]

        for (mean, variance) in department_params:
            threat_scores = generate_random_data(mean=mean, variance=variance, num_samples=100)
            dept_score = compute_department_score(threat_scores)
            department_scores.append(dept_score)

        # Compute the aggregated threat score
        aggregated_score = compute_aggregated_threat_score(department_scores, department_importance)
        print(f"Aggregated Score with extreme outliers in Finance: {aggregated_score}")
        self.assertTrue(0 <= aggregated_score <= 90, f"Aggregated score is out of range: {aggregated_score}")


# Run the unit tests
if __name__ == '__main__':
    unittest.main()
