# Requirements Document: SleepWise – AI Sleep Intelligence for Students

## Introduction

SleepWise is a full-stack web application designed to help students track sleep patterns, detect burnout risk, and receive intelligent recommendations through AI-driven pattern analysis. The system addresses the core problem that students have irregular sleep schedules due to academic stress, exams, and excessive screen time.

**What Makes SleepWise Different:**

Traditional sleep tracking apps are reactive and single-dimensional—they only measure sleep duration and provide generic advice. SleepWise is predictive and multi-dimensional, using AI-enhanced intelligence grounded in real-world student data to:

- **Correlate multiple factors**: Sleep duration, consistency, academic workload (study hours), pre-sleep screen time, mood, and exam stress are analyzed together to identify hidden patterns
- **Detect trends over time**: Rather than reacting to isolated bad nights, the system identifies deteriorating patterns and cumulative stress before they become critical
- **Provide context-aware recommendations**: Suggestions adapt based on the student's unique patterns, academic calendar, and historical data
- **Predict burnout risk**: Forward-looking analysis estimates future risk based on current trajectories, enabling early intervention
- **Calibrate using real student patterns**: Scoring thresholds and trend detection are informed by survey data collected from actual students, ensuring the system reflects real campus sleep patterns rather than theoretical ideals

The system combines rule-based logic with trend analysis and statistical correlation detection to deliver lightweight yet intelligent insights suitable for rapid development and real-world student use. Predictive intelligence uses rule-enhanced trend projection rather than complex machine learning, keeping the system hackathon-feasible while maintaining strong AI positioning.

## Glossary

- **System**: The SleepWise web application
- **User**: A student using the application to track sleep and wellness
- **Sleep_Entry**: A record containing sleep time, wake time, study hours, screen time, mood, and stress level
- **Sleep_Score**: A calculated value (0-100) representing overall sleep quality
- **Burnout_Risk**: A calculated assessment of whether the user is at risk of burnout
- **Dashboard**: The main interface displaying current sleep status and key metrics
- **Analytics_Page**: A page showing 7-day trends and correlations
- **Recommendation_Engine**: The component that generates personalized sleep suggestions
- **Sleep_Cycle**: A 90-minute period representing one complete sleep cycle
- **Survey_Data**: Anonymized and aggregated sleep data collected from real students via surveys
- **Campus_Baseline**: Statistical averages computed from survey data representing typical campus sleep patterns
- **Correlation_Coefficient**: A statistical measure (between -1 and 1) indicating the strength of relationship between two variables

## Requirements

### Requirement 1: Sleep Data Entry

**User Story:** As a student, I want to log my daily sleep and wellness data, so that I can track patterns over time.

#### Acceptance Criteria

1. WHEN a user accesses the input form page, THE System SHALL display fields for sleep time, wake time, study hours, screen time before bed, mood (1-5 scale), and exam stress level (1-5 scale)
2. WHEN a user submits a sleep entry with valid data, THE System SHALL store the entry with a timestamp
3. WHEN a user submits a sleep entry with invalid data (negative numbers, invalid time format), THE System SHALL reject the entry and display a descriptive error message
4. WHEN a user submits a sleep entry, THE System SHALL calculate and store the sleep duration automatically from sleep time and wake time
5. WHEN a sleep entry is stored, THE System SHALL persist the data to the database immediately

### Requirement 2: Sleep Score Calculation

**User Story:** As a student, I want to see a sleep quality score, so that I can understand how well I'm sleeping.

#### Acceptance Criteria

1. WHEN a sleep entry is submitted, THE System SHALL calculate a Sleep_Score between 0 and 100
2. THE Sleep_Score SHALL weight sleep duration at 40% where 7-8 hours receives full points and less than 6 hours receives heavy penalty
3. THE Sleep_Score SHALL weight consistency at 20% based on deviation in sleep time over the last 7 days
4. THE Sleep_Score SHALL apply a 15% screen time penalty where more than 60 minutes before bed reduces the score
5. THE Sleep_Score SHALL weight mood correlation at 15% where lower mood values reduce the score
6. THE Sleep_Score SHALL apply a 10% exam stress adjustment where higher stress levels affect the score
7. WHEN calculating consistency score, THE System SHALL use only available data if fewer than 7 days of history exist

### Requirement 3: Burnout Risk Detection

**User Story:** As a student, I want to be alerted when I'm at risk of burnout based on sustained patterns, so that I can take preventive action before reaching a crisis point.

#### Acceptance Criteria

1. WHEN a user has slept less than 6 hours for 3 consecutive days, THE System SHALL calculate a sustained sleep deficit indicator
2. WHEN a user's last 3 entries show study hours averaging greater than 5 AND mood averaging less than or equal to 2 AND stress averaging greater than or equal to 4, THE System SHALL calculate a cumulative stress indicator
3. WHEN either sustained sleep deficit OR cumulative stress indicators are triggered, THE System SHALL flag high burnout risk
4. WHEN high burnout risk is detected, THE System SHALL display the alert "⚠️ High Burnout Risk Detected. Prioritize rest." on the dashboard and burnout alert page with an explanation of which factors triggered the alert
5. WHEN burnout risk status changes, THE System SHALL update the display immediately
6. WHEN calculating burnout risk with fewer than 3 days of data, THE System SHALL use available data and indicate preliminary assessment

### Requirement 4: Predictive Insight & Trend Intelligence

**User Story:** As a student, I want the system to detect deteriorating patterns early, so that I can course-correct before my sleep quality becomes critical.

#### Acceptance Criteria

1. WHEN a user has 7 days of sleep data, THE System SHALL calculate a sleep pattern trend indicating whether sleep quality is improving, stable, or deteriorating
2. WHEN sleep duration decreases by more than 1 hour over a 7-day rolling window, THE System SHALL flag a deteriorating sleep pattern
3. WHEN a user accumulates sleep debt (cumulative difference between actual sleep and 7.5-hour target exceeding 5 hours over 7 days), THE System SHALL calculate and display the total sleep debt
4. WHEN current trends indicate the user will reach high burnout risk within 3 days if patterns continue, THE System SHALL display an early warning signal
5. WHEN early warning signals are triggered, THE System SHALL display a message explaining the projected risk and suggesting immediate adjustments
6. THE System SHALL recalculate trend intelligence daily when new sleep entries are added

### Requirement 5: AI Recommendation Engine

**User Story:** As a student, I want to receive personalized sleep recommendations that adapt to my patterns, so that I can improve my sleep quality effectively.

#### Acceptance Criteria

1. WHEN a user views recommendations, THE Recommendation_Engine SHALL analyze the most recent 7 days of data to identify patterns
2. WHEN a user views recommendations, THE Recommendation_Engine SHALL suggest an ideal sleep time based on their historical wake time and 7-8 hour sleep duration target
3. WHEN a user views recommendations, THE Recommendation_Engine SHALL calculate a smart wake-up time using 90-minute sleep cycle logic to avoid waking during deep sleep
4. WHEN a user's screen time before bed exceeds 60 minutes on average over 3 days, THE Recommendation_Engine SHALL suggest reducing screen time with specific target minutes
5. WHEN a user shows signs of sleep debt (average sleep less than 7 hours over 7 days), THE Recommendation_Engine SHALL suggest scheduling a recovery day
6. WHEN a user's mood correlates negatively with reduced sleep, THE Recommendation_Engine SHALL highlight this correlation in recommendations
7. THE Recommendation_Engine SHALL adapt suggestions based on detected trends rather than single-day anomalies

### Requirement 6: Dashboard Display

**User Story:** As a student, I want to see my current sleep status at a glance, so that I can quickly assess my wellness.

#### Acceptance Criteria

1. WHEN a user accesses the dashboard, THE System SHALL display the most recent Sleep_Score
2. WHEN a user accesses the dashboard, THE System SHALL display the current Burnout_Risk status
3. WHEN a user accesses the dashboard, THE System SHALL display personalized recommendations from the Recommendation_Engine
4. WHEN a user accesses the dashboard, THE System SHALL display a summary of the most recent sleep entry
5. THE Dashboard SHALL use dark mode as the default theme

### Requirement 7: Weekly Analytics Visualization

**User Story:** As a student, I want to visualize my sleep trends over time, so that I can identify patterns and correlations.

#### Acceptance Criteria

1. WHEN a user accesses the analytics page, THE System SHALL display a 7-day sleep duration trend graph
2. WHEN a user accesses the analytics page, THE System SHALL display a productivity versus sleep correlation chart showing study hours against sleep duration
3. WHEN a user accesses the analytics page, THE System SHALL display a mood trend line over the last 7 days
4. WHEN a user accesses the analytics page, THE System SHALL display a burnout risk meter showing current risk level
5. WHEN fewer than 7 days of data exist, THE System SHALL display available data and indicate incomplete dataset

### Requirement 8: Data Persistence

**User Story:** As a student, I want my sleep data to be saved reliably, so that I don't lose my tracking history.

#### Acceptance Criteria

1. WHEN a sleep entry is submitted, THE System SHALL persist the data to the database before confirming success to the user
2. WHEN the database is unavailable, THE System SHALL return an error message and prevent data loss
3. WHEN a user returns to the application, THE System SHALL retrieve all historical sleep entries from the database
4. THE System SHALL maintain data integrity by validating all entries before storage

### Requirement 9: User Interface Responsiveness

**User Story:** As a student, I want the application to be responsive and easy to use, so that I can quickly log my data on any device.

#### Acceptance Criteria

1. WHEN a user accesses the application on a mobile device, THE System SHALL display a responsive layout optimized for small screens
2. WHEN a user accesses the application on a desktop, THE System SHALL display a responsive layout optimized for large screens
3. WHEN a user navigates between pages, THE System SHALL complete navigation within 500 milliseconds
4. THE System SHALL use Tailwind CSS for consistent styling across all pages

### Requirement 10: Input Validation

**User Story:** As a student, I want the application to validate my input, so that I don't accidentally enter incorrect data.

#### Acceptance Criteria

1. WHEN a user enters a sleep time, THE System SHALL validate it is in HH:MM format
2. WHEN a user enters a wake time, THE System SHALL validate it is in HH:MM format
3. WHEN a user enters study hours, THE System SHALL validate it is a non-negative number
4. WHEN a user enters screen time, THE System SHALL validate it is a non-negative number in minutes
5. WHEN a user selects mood, THE System SHALL validate it is an integer between 1 and 5 inclusive
6. WHEN a user selects exam stress level, THE System SHALL validate it is an integer between 1 and 5 inclusive
7. WHEN validation fails, THE System SHALL display a specific error message indicating which field is invalid

### Requirement 11: Sleep Cycle Optimization

**User Story:** As a student, I want wake-up time suggestions based on sleep cycles, so that I wake up feeling refreshed.

#### Acceptance Criteria

1. WHEN calculating wake-up time, THE System SHALL use 90-minute sleep cycle intervals
2. WHEN a user's intended sleep duration doesn't align with complete sleep cycles, THE System SHALL suggest the nearest wake-up time that completes a full cycle
3. THE System SHALL prioritize wake-up times that result in 5 or 6 complete sleep cycles (7.5 or 9 hours)
4. WHEN displaying wake-up suggestions, THE System SHALL explain the sleep cycle rationale

### Requirement 12: AI-Driven Correlation Detection

**User Story:** As a student, I want the system to identify relationships between my sleep, mood, and academic workload, so that I can understand what factors most impact my wellness.

#### Acceptance Criteria

1. WHEN a user has at least 7 days of data, THE System SHALL calculate correlation coefficients between sleep duration and mood using lightweight statistical approximation
2. WHEN a user has at least 7 days of data, THE System SHALL calculate correlation coefficients between study hours and sleep quality using lightweight statistical approximation
3. WHEN a user has at least 7 days of data, THE System SHALL calculate correlation coefficients between screen time and sleep score using lightweight statistical approximation
4. WHEN strong correlations are detected (correlation coefficient magnitude greater than 0.6), THE System SHALL highlight these insights on the analytics page
5. WHEN displaying correlations, THE System SHALL provide plain-language explanations of what the correlation means for the user

### Requirement 13: Real-World Data Validation & Baseline Calibration

**User Story:** As a development team, we want to validate and calibrate the system using real student survey data, so that scoring logic and burnout thresholds reflect actual campus patterns.

#### Acceptance Criteria

1. WHEN survey responses are collected, THE System SHALL compute baseline metrics including average sleep duration, percentage sleeping less than 6 hours, average screen time before bed, and average stress level
2. WHEN initializing the system, THE System SHALL allow loading of aggregated survey averages as demo baseline data
3. WHERE the Campus Snapshot feature is enabled, THE Dashboard SHALL display a section showing anonymized aggregated statistics from survey data
4. WHEN displaying survey-derived data, THE System SHALL indicate that all survey data is anonymized and aggregated
5. THE System SHALL allow sleep score thresholds to be adjusted based on observed campus averages through configuration parameters
6. WHEN calibrating thresholds, THE System SHALL use lightweight statistical adjustments rather than complex machine learning models


