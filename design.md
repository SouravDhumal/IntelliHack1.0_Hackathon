# Design Document: SleepWise – AI Sleep Intelligence for Students

## 1. Overall Design Philosophy

SleepWise embodies a **dark futuristic aesthetic** that feels like a premium AI health-tech startup while remaining approachable and GenZ-friendly. The design prioritizes visual communication over text, using intelligent data visualization and subtle animations to create an engaging, modern experience.

### Core Design Principles

- **Dark-First Interface**: Deep, rich backgrounds that reduce eye strain during late-night usage
- **Visual Intelligence**: Data-driven cards with glowing indicators that communicate status at a glance
- **Minimal Cognitive Load**: Clean card-based layouts with clear visual hierarchy
- **Micro-Interactions**: Subtle animations that provide feedback without overwhelming
- **Glassmorphism Elements**: Soft transparency effects with backdrop blur for depth
- **Rounded Everything**: Smooth, friendly corners throughout (border-radius: 12-24px)
- **Gradient Accents**: Electric blue-to-purple gradients for AI-powered features
- **Responsive by Default**: Mobile-first approach that scales beautifully to desktop

### Technology Stack

- **Framework**: React 18+ with functional components and hooks
- **Styling**: Tailwind CSS with custom configuration
- **Charts**: Recharts (lightweight, React-native, customizable)
- **Animations**: CSS transitions + Framer Motion for complex interactions
- **Icons**: Lucide React (modern, consistent icon set)

---

## 2. Color System

### Primary Palette

```css
/* Background Layers */
--bg-primary: #0f172a;        /* Deep slate - main background */
--bg-secondary: #1e293b;      /* Lighter slate - cards */
--bg-tertiary: #334155;       /* Elevated elements */

/* Accent Colors */
--accent-primary: #3b82f6;    /* Electric blue */
--accent-secondary: #8b5cf6;  /* Purple */
--accent-gradient: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%);

/* Status Colors */
--success: #10b981;           /* Soft green */
--warning: #f59e0b;           /* Amber */
--danger: #ef4444;            /* Soft red */
--info: #06b6d4;              /* Cyan */

/* Text Colors */
--text-primary: #f1f5f9;      /* Off-white */
--text-secondary: #94a3b8;    /* Muted gray */
--text-tertiary: #64748b;     /* Darker gray */

/* Glow Effects */
--glow-blue: 0 0 20px rgba(59, 130, 246, 0.3);
--glow-purple: 0 0 20px rgba(139, 92, 246, 0.3);
--glow-green: 0 0 20px rgba(16, 185, 129, 0.3);
--glow-red: 0 0 20px rgba(239, 68, 68, 0.3);
```


### Usage Guidelines

**Backgrounds**: Use `bg-primary` for page backgrounds, `bg-secondary` for cards, `bg-tertiary` for nested elements or hover states.

**Accents**: Apply gradient to AI-powered features (score rings, insight cards). Use solid blue for interactive elements (buttons, links).

**Status Indicators**: 
- Green glow = Good/Healthy
- Amber glow = Warning/Moderate
- Red glow = Alert/Critical
- Blue glow = AI Insight/Information

**Text Hierarchy**: Primary text for headings and key metrics, secondary for labels and descriptions, tertiary for timestamps and metadata.

---

## 3. Layout Architecture

### Global Layout Structure

```
┌─────────────────────────────────────┐
│  Navigation Bar (sticky top)        │
├─────────────────────────────────────┤
│                                     │
│  Main Content Area                  │
│  (max-width: 1280px, centered)     │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  Page-Specific Content      │   │
│  │  (Grid/Flex layouts)        │   │
│  └─────────────────────────────┘   │
│                                     │
└─────────────────────────────────────┘
```

### Responsive Breakpoints

- **Mobile**: < 640px (single column, stacked cards)
- **Tablet**: 640px - 1024px (2-column grid where appropriate)
- **Desktop**: > 1024px (3-column grid, side-by-side layouts)

### Grid System

Use Tailwind's grid utilities with consistent gaps:
- Mobile: `gap-4` (1rem)
- Tablet/Desktop: `gap-6` (1.5rem)

---

## 4. Dashboard UI Design

**Route**: `/` or `/dashboard`

**Purpose**: Primary landing page showing current sleep status, AI insights, and quick actions.

### Layout Structure

```
┌──────────────────────────────────────────┐
│  Hero Section (Full Width)               │
│  ┌────────────┐  ┌──────────────────┐   │
│  │  Sleep     │  │  Burnout Risk    │   │
│  │  Score     │  │  Indicator       │   │
│  │  Ring      │  └──────────────────┘   │
│  └────────────┘                          │
├──────────────────────────────────────────┤
│  AI Insight Card (Full Width)            │
│  "Based on your patterns..."             │
├──────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐     │
│  │  7-Day       │  │  Sleep Debt  │     │
│  │  Trend       │  │  Meter       │     │
│  └──────────────┘  └──────────────┘     │
├──────────────────────────────────────────┤
│  Smart Recommendations (Grid)            │
│  ┌─────┐ ┌─────┐ ┌─────┐               │
│  │ Rec │ │ Rec │ │ Rec │               │
│  └─────┘ └─────┘ └─────┘               │
└──────────────────────────────────────────┘
```


### Component Breakdown

#### Hero Section (Top)

**Sleep Score Ring** (Left/Center on mobile)
- Large circular progress ring (200px diameter on desktop, 160px mobile)
- Animated stroke with gradient fill
- Score number in center (48px font, bold)
- Label "Sleep Score" below (14px, muted)
- Color coding:
  - 80-100: Green glow
  - 60-79: Blue glow
  - 40-59: Amber glow
  - 0-39: Red glow

**Burnout Risk Badge** (Right/Below on mobile)
- Rounded pill badge with glow effect
- Icon + Text layout
- States:
  - Low Risk: Green background, checkmark icon
  - Moderate Risk: Amber background, alert icon
  - High Risk: Red background, warning icon
- Pulsing animation when High Risk

#### AI Insight Card

- Full-width card with glassmorphism effect
- Gradient border (1px, blue-purple)
- Sparkle/brain icon in top-left
- Auto-generated summary text (16px, primary color)
- Subtle background pattern or mesh gradient
- Example: "Your sleep consistency has improved by 15% this week. Keep it up! 🌙"

#### 7-Day Trend Mini Graph

- Compact line chart (height: 120px)
- X-axis: Last 7 days (abbreviated day names)
- Y-axis: Sleep hours (4-10 range)
- Gradient fill under line
- Target line at 7.5 hours (dashed, muted)
- Hover tooltip showing exact values

#### Sleep Debt Meter

- Horizontal progress bar
- Shows accumulated sleep debt vs. 5-hour threshold
- Color transitions from green → amber → red
- Label: "Sleep Debt: X.X hours"
- Subtitle: "Target: < 5 hours"

#### Smart Recommendations Grid

- 3-column grid on desktop, 1-column on mobile
- Each recommendation card:
  - Icon at top (24px)
  - Title (16px, bold)
  - Description (14px, secondary color)
  - Rounded corners (16px)
  - Hover: slight elevation + glow
- Examples:
  - 🛏️ "Sleep by 11:30 PM tonight"
  - 📱 "Reduce screen time to 30 min"
  - ⏰ "Wake at 7:00 AM for optimal cycle"

### Responsive Behavior

**Desktop (> 1024px)**:
- Hero section: 2-column (score left, burnout right)
- Trend + Debt: 2-column side-by-side
- Recommendations: 3-column grid

**Tablet (640-1024px)**:
- Hero section: 2-column (smaller)
- Trend + Debt: 2-column
- Recommendations: 2-column grid

**Mobile (< 640px)**:
- All elements stack vertically
- Score ring centered, slightly smaller
- Single column for all cards
- Recommendations: 1-column, full-width

---

## 5. Sleep Entry Form Page

**Route**: `/entry` or `/log-sleep`

**Purpose**: Input form for daily sleep and wellness data.

### Layout Structure

```
┌──────────────────────────────────────┐
│  Page Header                         │
│  "Log Your Sleep"                    │
├──────────────────────────────────────┤
│  Form Card (Centered, max-w-2xl)    │
│  ┌────────────────────────────────┐ │
│  │  Sleep Time Input              │ │
│  │  Wake Time Input               │ │
│  │  ─────────────────             │ │
│  │  Study Hours Slider            │ │
│  │  Screen Time Slider            │ │
│  │  ─────────────────             │ │
│  │  Mood Scale (1-5)              │ │
│  │  Stress Scale (1-5)            │ │
│  │  ─────────────────             │ │
│  │  [Submit Button]               │ │
│  └────────────────────────────────┘ │
└──────────────────────────────────────┘
```


### Component Breakdown

#### Time Inputs
- Custom styled time pickers with dark theme
- Large, touch-friendly inputs (48px height)
- Clock icon prefix
- Format: HH:MM with AM/PM toggle
- Validation feedback inline (red border + message)

#### Slider Inputs (Study Hours, Screen Time)
- Custom range sliders with gradient track
- Current value displayed above thumb
- Min/Max labels at ends
- Smooth dragging with haptic-like feedback
- Study Hours: 0-12 hours
- Screen Time: 0-180 minutes

#### Scale Inputs (Mood, Stress)
- 5-button horizontal radio group
- Each button: emoji + number
- Mood: 😢 😕 😐 🙂 😊 (1-5)
- Stress: 😌 🙂 😐 😰 😫 (1-5)
- Selected state: gradient background + glow
- Unselected: muted background

#### Submit Button
- Full-width gradient button
- Large (56px height)
- Text: "Save Sleep Entry"
- Loading state: spinner + "Saving..."
- Success state: checkmark + "Saved!" (brief)
- Disabled state when form invalid

### Form Validation

- Real-time validation on blur
- Error messages appear below fields
- Red border + red text for errors
- Green checkmark when valid
- Prevent submission if any field invalid

### Responsive Behavior

- Form card: max-width 672px, centered
- Mobile: Full-width with padding
- All inputs stack vertically
- Consistent spacing (gap-6)

---

## 6. Analytics Page UI

**Route**: `/analytics`

**Purpose**: Visualize 7-day trends, correlations, and patterns.

### Layout Structure

```
┌──────────────────────────────────────────┐
│  Page Header + Date Range                │
├──────────────────────────────────────────┤
│  Sleep Duration Trend (Full Width)       │
│  [Large Line Chart]                      │
├──────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐     │
│  │  Mood Trend  │  │  Burnout     │     │
│  │  Chart       │  │  Risk Meter  │     │
│  └──────────────┘  └──────────────┘     │
├──────────────────────────────────────────┤
│  Productivity vs Sleep (Full Width)      │
│  [Scatter Plot]                          │
├──────────────────────────────────────────┤
│  Correlation Insights (Grid)             │
│  ┌─────┐ ┌─────┐ ┌─────┐               │
│  │ Cor │ │ Cor │ │ Cor │               │
│  └─────┘ └─────┘ └─────┘               │
└──────────────────────────────────────────┘
```


### Component Breakdown

#### Sleep Duration Trend Chart
- Large line chart (height: 300px)
- X-axis: Last 7 days (Mon, Tue, Wed...)
- Y-axis: Hours (0-12)
- Gradient fill under line (blue-purple)
- Target zone (7-8 hours) highlighted with subtle background
- Data points: circles with hover tooltip
- Smooth curve interpolation
- Grid lines: subtle, dashed

#### Mood Trend Chart
- Smaller line chart (height: 200px)
- X-axis: Last 7 days
- Y-axis: Mood scale (1-5)
- Color-coded line (red → green gradient)
- Emoji markers at data points
- Hover shows mood + date

#### Burnout Risk Meter
- Vertical gauge or semi-circular meter
- Color zones: Green (Low) → Amber (Moderate) → Red (High)
- Animated needle pointing to current risk
- Percentage or level indicator
- Factors list below (what's contributing)

#### Productivity vs Sleep Scatter Plot
- X-axis: Sleep hours (4-10)
- Y-axis: Study hours (0-12)
- Each point: one day's data
- Color-coded by mood (red to green)
- Trend line if correlation detected
- Hover: shows date + exact values
- Height: 280px

#### Correlation Insight Cards
- 3-column grid (1-column mobile)
- Each card shows:
  - Correlation strength (Strong/Moderate/Weak)
  - Icon representing relationship
  - Variables (e.g., "Sleep ↔ Mood")
  - Correlation coefficient (r = X.XX)
  - Plain-language explanation
  - Visual indicator (up/down arrows, color)
- Example: "Strong positive correlation between sleep and mood (r = 0.78). More sleep = better mood! 📈"

### Chart Styling (Recharts Configuration)

```javascript
// Common chart theme
const chartTheme = {
  backgroundColor: 'transparent',
  textColor: '#94a3b8',
  gridColor: '#334155',
  lineColor: '#3b82f6',
  gradientStart: '#3b82f6',
  gradientEnd: '#8b5cf6',
  tooltipBg: '#1e293b',
  tooltipBorder: '#3b82f6',
}
```

### Responsive Behavior

- Desktop: 2-column layout for mood + burnout
- Tablet: 2-column maintained
- Mobile: All charts stack, full-width
- Chart heights reduce slightly on mobile

---

## 7. Burnout Alert View

**Route**: `/burnout-alert` (or modal overlay on dashboard)

**Purpose**: Dramatic but supportive alert when high burnout risk detected.

### Layout Structure

```
┌──────────────────────────────────────┐
│  [Subtle red gradient background]   │
│                                      │
│  ┌────────────────────────────────┐ │
│  │  ⚠️ Large Alert Icon           │ │
│  │                                │ │
│  │  "High Burnout Risk Detected"  │ │
│  │                                │ │
│  │  Explanation Text              │ │
│  │  "You've slept < 6 hours for   │ │
│  │   3 consecutive days..."       │ │
│  │                                │ │
│  │  Triggered Factors:            │ │
│  │  • Sleep Deficit               │ │
│  │  • High Stress                 │ │
│  │  • Low Mood                    │ │
│  │                                │ │
│  │  Recovery Actions:             │ │
│  │  ┌─────┐ ┌─────┐ ┌─────┐     │ │
│  │  │ Act │ │ Act │ │ Act │     │ │
│  │  └─────┘ └─────┘ └─────┘     │ │
│  │                                │ │
│  │  [Acknowledge Button]          │ │
│  └────────────────────────────────┘ │
└──────────────────────────────────────┘
```


### Component Breakdown

#### Background Effect
- Subtle radial gradient from center
- Base: `bg-primary` (#0f172a)
- Overlay: Radial red glow (rgba(239, 68, 68, 0.1))
- Not overwhelming, just a hint of urgency

#### Alert Icon
- Large warning icon (80px)
- Animated pulse effect (scale 1 → 1.05 → 1)
- Red-orange gradient fill
- Soft glow around icon

#### Heading
- Large, bold text (32px)
- Primary text color
- Centered alignment
- Margin below for spacing

#### Explanation Text
- 18px font size
- Secondary text color
- Max-width: 600px, centered
- Explains what triggered the alert
- Supportive tone, not fear-based

#### Triggered Factors List
- Bullet list with icons
- Each factor: icon + label
- Color-coded by severity
- Examples:
  - 🛏️ Sleep Deficit (< 6 hrs for 3 days)
  - 😰 High Stress (avg 4.5/5)
  - 😔 Low Mood (avg 2/5)

#### Recovery Action Cards
- 3-column grid (1-column mobile)
- Each card:
  - Icon at top
  - Action title (bold)
  - Brief description
  - Rounded, elevated card
  - Hover: slight lift
- Examples:
  - 🌙 "Schedule 8+ hours tonight"
  - 🧘 "Take a 20-min break"
  - 💬 "Talk to someone you trust"

#### Acknowledge Button
- Large button (56px height)
- Gradient background (blue-purple)
- Text: "I Understand, Take Me Back"
- Dismisses alert, returns to dashboard

### Tone & Messaging

- Supportive, not alarmist
- Empowering language
- Focus on actionable steps
- Acknowledge difficulty of student life
- Example: "We noticed some concerning patterns. Let's work together to get you back on track. 💙"

---

## 8. Campus Snapshot Panel

**Location**: Dashboard (bottom section) or separate `/campus-stats` page

**Purpose**: Display anonymized, aggregated sleep data from real student surveys.

### Layout Structure

```
┌──────────────────────────────────────────┐
│  Section Header                          │
│  "Campus Sleep Snapshot"                 │
│  "Anonymized data from 100+ students"    │
├──────────────────────────────────────────┤
│  Stats Grid (4 columns, 2 on tablet)    │
│  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
│  │ Avg │ │  %  │ │ Avg │ │Stress│      │
│  │Sleep│ │Depr.│ │Scrn │ │Level │      │
│  └─────┘ └─────┘ └─────┘ └─────┘       │
└──────────────────────────────────────────┘
```

### Component Breakdown

#### Section Header
- Title: "Campus Sleep Snapshot" (24px, bold)
- Subtitle: "Anonymized data from [N] students" (14px, muted)
- Info icon with tooltip explaining data privacy

#### Stat Cards
- Compact, uniform cards
- Icon at top (32px)
- Large metric value (36px, bold, gradient text)
- Label below (14px, secondary)
- Subtle background glow matching metric color

**Card 1: Average Campus Sleep**
- Icon: 🌙 or bed icon
- Metric: "6.4 hours"
- Label: "Avg Sleep Duration"
- Color: Blue

**Card 2: % Sleep Deprived**
- Icon: ⚠️ or alert icon
- Metric: "42%"
- Label: "Sleeping < 6 hours"
- Color: Amber/Red

**Card 3: Average Screen Time**
- Icon: 📱 or phone icon
- Metric: "78 min"
- Label: "Before Bed"
- Color: Purple

**Card 4: Stress Level**
- Icon: 😰 or stress icon
- Metric: "3.8 / 5"
- Label: "Avg Stress Level"
- Color: Orange

### Data Privacy Notice

- Small text below stats
- "All data is anonymized and aggregated. No individual information is shared."
- Link to privacy policy (if applicable)

### Responsive Behavior

- Desktop: 4-column grid
- Tablet: 2x2 grid
- Mobile: 2x2 grid (smaller cards) or 1-column

---

## 9. Component Design System

### Reusable Components Library


#### 1. Insight Card

**Purpose**: Display AI-generated insights and recommendations.

**Structure**:
```jsx
<div className="insight-card">
  <div className="icon">{/* Sparkle/Brain icon */}</div>
  <p className="insight-text">{insightText}</p>
</div>
```

**Styling**:
- Background: `bg-secondary` with glassmorphism
- Border: 1px gradient (blue-purple)
- Padding: 24px
- Border-radius: 16px
- Backdrop blur: 10px
- Box-shadow: Soft glow

**Variants**:
- Default: Blue gradient border
- Warning: Amber gradient border
- Success: Green gradient border

---

#### 2. Metric Card

**Purpose**: Display single key metrics with icon and label.

**Structure**:
```jsx
<div className="metric-card">
  <div className="icon">{/* Icon */}</div>
  <div className="value">{metricValue}</div>
  <div className="label">{metricLabel}</div>
</div>
```

**Styling**:
- Background: `bg-secondary`
- Padding: 20px
- Border-radius: 12px
- Text-align: center
- Hover: Slight elevation (translateY: -2px)
- Transition: all 0.2s ease

**Variants**:
- Small: 120px width
- Medium: 180px width
- Large: 240px width

---

#### 3. Glow Badge

**Purpose**: Status indicators with glow effects.

**Structure**:
```jsx
<div className="glow-badge" data-status={status}>
  <span className="icon">{icon}</span>
  <span className="text">{text}</span>
</div>
```

**Styling**:
- Display: inline-flex
- Padding: 8px 16px
- Border-radius: 24px (pill shape)
- Font-size: 14px
- Font-weight: 600
- Box-shadow: Status-based glow

**Status Variants**:
- `success`: Green background + green glow
- `warning`: Amber background + amber glow
- `danger`: Red background + red glow + pulse animation
- `info`: Blue background + blue glow

---

#### 4. Trend Indicator

**Purpose**: Show directional change with arrow and percentage.

**Structure**:
```jsx
<div className="trend-indicator" data-direction={direction}>
  <span className="arrow">{arrow}</span>
  <span className="value">{percentage}%</span>
</div>
```

**Styling**:
- Display: inline-flex
- Gap: 4px
- Font-size: 14px
- Font-weight: 600

**Direction Variants**:
- `up`: Green color, ↑ arrow
- `down`: Red color, ↓ arrow
- `neutral`: Gray color, → arrow

---

#### 5. Animated Circular Score Ring

**Purpose**: Display sleep score with animated progress ring.

**Structure**:
```jsx
<div className="score-ring">
  <svg className="ring-svg">
    <circle className="ring-background" />
    <circle className="ring-progress" strokeDasharray={circumference} strokeDashoffset={offset} />
  </svg>
  <div className="ring-content">
    <div className="score-value">{score}</div>
    <div className="score-label">Sleep Score</div>
  </div>
</div>
```

**Styling**:
- Size: 200px diameter (desktop), 160px (mobile)
- Ring width: 12px
- Background ring: `bg-tertiary`
- Progress ring: Gradient stroke (blue-purple)
- Animation: Stroke-dashoffset transition (1s ease-out)
- Glow: Color-coded based on score

**Animation**:
- On mount: Animate from 0 to actual score
- Duration: 1 second
- Easing: ease-out

**Color Coding**:
- 80-100: Green gradient + green glow
- 60-79: Blue gradient + blue glow
- 40-59: Amber gradient + amber glow
- 0-39: Red gradient + red glow

---

#### 6. Risk Level Indicator

**Purpose**: Visual representation of burnout risk level.

**Structure**:
```jsx
<div className="risk-indicator" data-level={riskLevel}>
  <div className="risk-bar">
    <div className="risk-fill" style={{width: `${percentage}%`}} />
  </div>
  <div className="risk-label">{riskLevel} Risk</div>
</div>
```

**Styling**:
- Bar height: 8px
- Border-radius: 4px
- Background: `bg-tertiary`
- Fill: Gradient based on risk level
- Transition: width 0.5s ease

**Risk Levels**:
- Low (0-33%): Green gradient
- Moderate (34-66%): Amber gradient
- High (67-100%): Red gradient + pulse animation

---

### Component Interaction Patterns

**Hover States**:
- Cards: Slight elevation (translateY: -2px) + increased shadow
- Buttons: Brightness increase (110%)
- Links: Underline + color shift

**Active States**:
- Buttons: Scale down (0.98)
- Cards: No change (prevent layout shift)

**Focus States**:
- All interactive elements: 2px blue outline with offset
- Keyboard navigation friendly

**Loading States**:
- Skeleton screens with shimmer effect
- Spinner for async actions
- Disabled state for buttons (opacity: 0.5)

---

## 10. Micro-Interactions

### Animation Specifications


#### 1. Score Ring Animation

**Trigger**: Component mount or score update

**Animation**:
```css
@keyframes scoreRingFill {
  from {
    stroke-dashoffset: circumference;
  }
  to {
    stroke-dashoffset: calculatedOffset;
  }
}

.ring-progress {
  animation: scoreRingFill 1s ease-out forwards;
}
```

**Details**:
- Duration: 1 second
- Easing: ease-out (starts fast, ends slow)
- Delay: 200ms after page load
- Accompanied by number count-up animation

---

#### 2. Burnout Indicator Pulse

**Trigger**: High burnout risk detected

**Animation**:
```css
@keyframes pulse {
  0%, 100% {
    transform: scale(1);
    box-shadow: 0 0 20px rgba(239, 68, 68, 0.3);
  }
  50% {
    transform: scale(1.05);
    box-shadow: 0 0 30px rgba(239, 68, 68, 0.5);
  }
}

.burnout-badge[data-risk="high"] {
  animation: pulse 2s ease-in-out infinite;
}
```

**Details**:
- Duration: 2 seconds
- Infinite loop
- Subtle scale change (1 → 1.05)
- Glow intensity increases at peak

---

#### 3. Card Hover Elevation

**Trigger**: Mouse hover over interactive cards

**Animation**:
```css
.card {
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}
```

**Details**:
- Duration: 200ms
- Easing: ease
- Lift: 4px upward
- Shadow increases for depth

---

#### 4. Chart Transitions

**Trigger**: Data update or page load

**Animation**:
```css
/* Line chart path animation */
@keyframes drawLine {
  from {
    stroke-dashoffset: pathLength;
  }
  to {
    stroke-dashoffset: 0;
  }
}

/* Bar chart height animation */
@keyframes growBar {
  from {
    transform: scaleY(0);
  }
  to {
    transform: scaleY(1);
  }
}
```

**Details**:
- Line charts: Draw from left to right (1.5s)
- Bar charts: Grow from bottom to top (0.8s)
- Stagger delay: 50ms between elements
- Easing: ease-out

---

#### 5. Button Click Feedback

**Trigger**: Button click/tap

**Animation**:
```css
.button {
  transition: transform 0.1s ease;
}

.button:active {
  transform: scale(0.98);
}
```

**Details**:
- Duration: 100ms
- Scale down slightly (0.98)
- Immediate feedback
- Returns to normal on release

---

#### 6. Page Transitions

**Trigger**: Route change

**Animation**:
```css
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.page-content {
  animation: fadeIn 0.3s ease-out;
}
```

**Details**:
- Duration: 300ms
- Fade in + slight upward movement
- Easing: ease-out
- Applies to main content area

---

#### 7. Tooltip Appearance

**Trigger**: Hover over chart data points or info icons

**Animation**:
```css
@keyframes tooltipFade {
  from {
    opacity: 0;
    transform: translateY(-5px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.tooltip {
  animation: tooltipFade 0.15s ease-out;
}
```

**Details**:
- Duration: 150ms
- Quick fade-in
- Slight downward movement
- Positioned near cursor/element

---

### Animation Performance Guidelines

- Use `transform` and `opacity` for animations (GPU-accelerated)
- Avoid animating `width`, `height`, `top`, `left` (causes reflow)
- Use `will-change` sparingly for complex animations
- Prefer CSS transitions over JavaScript animations
- Keep animation durations under 1 second for UI feedback
- Use `prefers-reduced-motion` media query for accessibility

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 11. Typography System

### Font Stack

```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', sans-serif;
```

**Rationale**: Inter is modern, highly legible, and optimized for screens. Fallbacks ensure consistency across platforms.

### Type Scale

```css
/* Headings */
--text-4xl: 48px;  /* Hero headings */
--text-3xl: 36px;  /* Page titles */
--text-2xl: 30px;  /* Section headings */
--text-xl: 24px;   /* Card titles */
--text-lg: 20px;   /* Subheadings */

/* Body */
--text-base: 16px; /* Default body text */
--text-sm: 14px;   /* Secondary text, labels */
--text-xs: 12px;   /* Captions, metadata */

/* Special */
--text-display: 64px; /* Large score numbers */
```

### Font Weights

```css
--font-normal: 400;   /* Body text */
--font-medium: 500;   /* Emphasis */
--font-semibold: 600; /* Headings */
--font-bold: 700;     /* Strong emphasis */
```

### Line Heights

```css
--leading-tight: 1.2;   /* Headings */
--leading-normal: 1.5;  /* Body text */
--leading-relaxed: 1.75; /* Long-form content */
```

### Usage Guidelines

**Headings**:
- Use semibold or bold weights
- Primary text color
- Tight line-height
- Generous margin-bottom

**Body Text**:
- Use normal weight
- Secondary text color for descriptions
- Normal line-height
- Max-width: 65ch for readability

**Labels**:
- Use small size (14px)
- Medium weight
- Tertiary text color
- Uppercase optional for emphasis

**Numbers/Metrics**:
- Use bold weight
- Larger size for emphasis
- Gradient text for key metrics
- Tabular numbers (font-variant-numeric: tabular-nums)

---

## 12. Navigation & Routing

### Navigation Bar

**Position**: Sticky top, full-width

**Structure**:
```
┌────────────────────────────────────────┐
│  Logo  |  Dashboard  Analytics  Entry │
└────────────────────────────────────────┘
```

**Styling**:
- Background: `bg-secondary` with backdrop blur
- Height: 64px
- Border-bottom: 1px solid `bg-tertiary`
- Box-shadow: Subtle shadow when scrolled

**Logo**:
- Left-aligned
- Icon + "SleepWise" text
- Gradient text effect
- Links to dashboard

**Nav Links**:
- Right-aligned (desktop), hamburger menu (mobile)
- Horizontal list
- Active state: Gradient underline
- Hover: Text color brightens

**Mobile Menu**:
- Hamburger icon (top-right)
- Slide-in drawer from right
- Full-height overlay
- Close button at top

### Route Structure

```
/                    → Dashboard (default)
/dashboard           → Dashboard (alias)
/entry               → Sleep Entry Form
/analytics           → Analytics Page
/burnout-alert       → Burnout Alert View
/campus-stats        → Campus Snapshot (optional standalone)
```

### Page Transitions

- Fade-in animation (300ms)
- Scroll to top on route change
- Loading state for async data

---

## 13. Responsive Design Strategy

### Breakpoint System

```css
/* Tailwind default breakpoints */
sm: 640px   /* Small tablets, large phones */
md: 768px   /* Tablets */
lg: 1024px  /* Small laptops */
xl: 1280px  /* Desktops */
2xl: 1536px /* Large desktops */
```

### Mobile-First Approach

Design for mobile first, then enhance for larger screens:

1. **Base styles** (< 640px): Single column, stacked layout
2. **Tablet** (640px+): 2-column grids where appropriate
3. **Desktop** (1024px+): 3-column grids, side-by-side layouts

### Component Responsiveness

**Dashboard**:
- Mobile: All cards stack vertically
- Tablet: Score + Burnout side-by-side, rest stacked
- Desktop: Full grid layout

**Analytics**:
- Mobile: All charts full-width, stacked
- Tablet: 2-column for smaller charts
- Desktop: Optimized chart sizes

**Forms**:
- Mobile: Full-width inputs, larger touch targets
- Tablet/Desktop: Centered, max-width container

### Touch Targets

- Minimum size: 44x44px (iOS guideline)
- Generous padding on buttons
- Adequate spacing between interactive elements

### Performance Considerations

- Lazy load charts on scroll
- Optimize images (use WebP with fallbacks)
- Code splitting by route
- Minimize bundle size (tree-shaking)

---

## 14. Accessibility (A11y)

### WCAG 2.1 AA Compliance

**Color Contrast**:
- Text on background: Minimum 4.5:1 ratio
- Large text (18px+): Minimum 3:1 ratio
- Interactive elements: Clear focus indicators

**Keyboard Navigation**:
- All interactive elements accessible via Tab
- Logical tab order
- Skip-to-content link
- Escape key closes modals/menus

**Screen Reader Support**:
- Semantic HTML (nav, main, article, etc.)
- ARIA labels for icons and complex components
- Alt text for images
- Live regions for dynamic content updates

**Focus Management**:
- Visible focus indicators (2px blue outline)
- Focus trap in modals
- Return focus after modal close

**Motion & Animation**:
- Respect `prefers-reduced-motion`
- Provide option to disable animations
- No auto-playing videos

### Accessibility Checklist

- [ ] All images have alt text
- [ ] Form inputs have associated labels
- [ ] Color is not the only means of conveying information
- [ ] Sufficient color contrast throughout
- [ ] Keyboard navigation works for all features
- [ ] Screen reader testing completed
- [ ] Focus indicators visible and clear
- [ ] ARIA attributes used correctly
- [ ] Headings follow logical hierarchy
- [ ] Error messages are descriptive and helpful

---

## 15. Technical Implementation Notes

### Project Structure

```
src/
├── components/
│   ├── common/
│   │   ├── Button.jsx
│   │   ├── Card.jsx
│   │   ├── Badge.jsx
│   │   └── ScoreRing.jsx
│   ├── charts/
│   │   ├── LineChart.jsx
│   │   ├── ScatterPlot.jsx
│   │   └── GaugeChart.jsx
│   ├── dashboard/
│   │   ├── Dashboard.jsx
│   │   ├── AIInsightCard.jsx
│   │   └── RecommendationGrid.jsx
│   ├── analytics/
│   │   ├── Analytics.jsx
│   │   └── CorrelationCard.jsx
│   └── forms/
│       ├── SleepEntryForm.jsx
│       └── FormInput.jsx
├── pages/
│   ├── DashboardPage.jsx
│   ├── AnalyticsPage.jsx
│   ├── EntryPage.jsx
│   └── BurnoutAlertPage.jsx
├── hooks/
│   ├── useSleepData.js
│   ├── useScoreCalculation.js
│   └── useBurnoutDetection.js
├── utils/
│   ├── calculations.js
│   ├── dateHelpers.js
│   └── chartConfig.js
├── styles/
│   └── globals.css
└── App.jsx
```


### Tailwind Configuration

```javascript
// tailwind.config.js
module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'],
  theme: {
    extend: {
      colors: {
        primary: {
          bg: '#0f172a',
          card: '#1e293b',
          elevated: '#334155',
        },
        accent: {
          blue: '#3b82f6',
          purple: '#8b5cf6',
          cyan: '#06b6d4',
        },
        status: {
          success: '#10b981',
          warning: '#f59e0b',
          danger: '#ef4444',
        },
        text: {
          primary: '#f1f5f9',
          secondary: '#94a3b8',
          tertiary: '#64748b',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        'glow-blue': '0 0 20px rgba(59, 130, 246, 0.3)',
        'glow-purple': '0 0 20px rgba(139, 92, 246, 0.3)',
        'glow-green': '0 0 20px rgba(16, 185, 129, 0.3)',
        'glow-red': '0 0 20px rgba(239, 68, 68, 0.3)',
      },
      animation: {
        'pulse-slow': 'pulse 2s ease-in-out infinite',
        'fade-in': 'fadeIn 0.3s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0', transform: 'translateY(10px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
      },
    },
  },
  plugins: [],
}
```

### Chart Library Setup (Recharts)

```bash
npm install recharts
```

**Example Line Chart Component**:
```jsx
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const SleepTrendChart = ({ data }) => {
  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <defs>
          <linearGradient id="colorSleep" x1="0" y1="0" x2="0" y2="1">
            <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.8}/>
            <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0.1}/>
          </linearGradient>
        </defs>
        <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
        <XAxis dataKey="day" stroke="#94a3b8" />
        <YAxis stroke="#94a3b8" />
        <Tooltip 
          contentStyle={{ 
            backgroundColor: '#1e293b', 
            border: '1px solid #3b82f6',
            borderRadius: '8px'
          }} 
        />
        <Line 
          type="monotone" 
          dataKey="hours" 
          stroke="#3b82f6" 
          strokeWidth={2}
          fill="url(#colorSleep)" 
        />
      </LineChart>
    </ResponsiveContainer>
  );
};
```

### State Management

**Recommendation**: Use React Context API + useReducer for global state (lightweight, no external dependencies).

**Alternative**: If complexity grows, consider Zustand (minimal, modern state management).

**State Structure**:
```javascript
{
  sleepEntries: [],
  currentScore: null,
  burnoutRisk: 'low',
  recommendations: [],
  campusStats: {},
  loading: false,
  error: null,
}
```

### API Integration

**Backend Endpoints** (assumed):
```
POST   /api/sleep-entries      → Create new entry
GET    /api/sleep-entries      → Get all entries
GET    /api/sleep-score        → Get current score
GET    /api/burnout-risk       → Get burnout status
GET    /api/recommendations    → Get AI recommendations
GET    /api/analytics          → Get 7-day analytics data
GET    /api/campus-stats       → Get aggregated campus data
```

**Fetch Example**:
```javascript
const submitSleepEntry = async (entryData) => {
  try {
    const response = await fetch('/api/sleep-entries', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(entryData),
    });
    if (!response.ok) throw new Error('Failed to submit entry');
    return await response.json();
  } catch (error) {
    console.error('Error submitting sleep entry:', error);
    throw error;
  }
};
```

### Performance Optimization

1. **Code Splitting**: Use React.lazy() for route-based splitting
2. **Memoization**: Use React.memo() for expensive components
3. **Debouncing**: Debounce form inputs and search
4. **Lazy Loading**: Load charts only when visible (Intersection Observer)
5. **Image Optimization**: Use WebP format, lazy load images
6. **Bundle Analysis**: Use webpack-bundle-analyzer to identify bloat

### Testing Strategy

**Unit Tests**:
- Calculation functions (sleep score, burnout detection)
- Utility functions (date helpers, formatters)
- Custom hooks

**Component Tests**:
- Form validation
- Button interactions
- Card rendering

**Integration Tests**:
- Full user flows (entry submission → dashboard update)
- API integration

**Tools**: Jest + React Testing Library

### Browser Support

- Chrome/Edge: Last 2 versions
- Firefox: Last 2 versions
- Safari: Last 2 versions
- Mobile Safari: iOS 13+
- Chrome Mobile: Android 8+

### Deployment Considerations

- **Build**: `npm run build` (optimized production build)
- **Environment Variables**: Use `.env` for API endpoints
- **CDN**: Serve static assets via CDN
- **Caching**: Implement service worker for offline support (optional)
- **Analytics**: Integrate privacy-friendly analytics (Plausible, Fathom)

---

## 16. Dark Mode Implementation

### Default Dark Theme

SleepWise uses dark mode as the default and only theme (no light mode toggle needed for hackathon scope).

### CSS Variables Approach

```css
:root {
  /* Background colors */
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-tertiary: #334155;
  
  /* Text colors */
  --text-primary: #f1f5f9;
  --text-secondary: #94a3b8;
  --text-tertiary: #64748b;
  
  /* Accent colors */
  --accent-blue: #3b82f6;
  --accent-purple: #8b5cf6;
  
  /* Status colors */
  --success: #10b981;
  --warning: #f59e0b;
  --danger: #ef4444;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
}
```

### Glassmorphism Effect

```css
.glass-card {
  background: rgba(30, 41, 59, 0.7);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}
```

---

## 17. Error Handling & Edge Cases

### Empty States

**No Sleep Data**:
- Display friendly illustration
- Message: "No sleep data yet. Log your first entry to get started!"
- Prominent CTA button: "Log Sleep"

**Insufficient Data for Analytics**:
- Show partial data with disclaimer
- Message: "We need at least 7 days of data for full analytics. Keep logging!"
- Progress indicator: "3/7 days logged"

### Error States

**API Failure**:
- Toast notification: "Oops! Something went wrong. Please try again."
- Retry button
- Fallback to cached data if available

**Form Validation Errors**:
- Inline error messages (red text below field)
- Prevent submission until resolved
- Clear, specific error text

**Network Offline**:
- Banner at top: "You're offline. Data will sync when reconnected."
- Queue actions for later sync

### Loading States

**Initial Page Load**:
- Skeleton screens matching layout
- Shimmer animation
- No jarring content shifts

**Data Fetching**:
- Spinner for small actions
- Progress bar for longer operations
- Optimistic UI updates where possible

---

## 18. Future Enhancements (Post-Hackathon)

### Phase 2 Features

1. **User Authentication**: Login/signup, personalized data
2. **Social Features**: Compare with friends (anonymized)
3. **Notifications**: Reminders to log sleep, bedtime alerts
4. **Wearable Integration**: Import data from Fitbit, Apple Watch
5. **Advanced AI**: Machine learning models for better predictions
6. **Gamification**: Streaks, badges, achievements
7. **Export Data**: Download CSV, PDF reports
8. **Dark/Light Mode Toggle**: User preference
9. **Internationalization**: Multi-language support
10. **Progressive Web App**: Offline support, installable

### Scalability Considerations

- Database indexing for faster queries
- Caching layer (Redis) for frequently accessed data
- Rate limiting on API endpoints
- Horizontal scaling for increased traffic
- CDN for global distribution

---

## 19. Design Handoff Checklist

### For Developers

- [ ] Tailwind config file created with custom colors
- [ ] Component library structure established
- [ ] Recharts installed and configured
- [ ] Responsive breakpoints tested
- [ ] Animations implemented with CSS transitions
- [ ] Accessibility features verified
- [ ] Dark theme applied globally
- [ ] Form validation logic implemented
- [ ] Error handling in place
- [ ] Loading states for all async operations

### Design Assets

- [ ] Logo files (SVG, PNG)
- [ ] Icon set (Lucide React)
- [ ] Color palette documented
- [ ] Typography scale defined
- [ ] Component examples created
- [ ] Spacing system established
- [ ] Shadow/glow effects documented

### Testing

- [ ] Mobile responsiveness verified (iOS, Android)
- [ ] Desktop browsers tested (Chrome, Firefox, Safari)
- [ ] Keyboard navigation works
- [ ] Screen reader compatibility checked
- [ ] Performance metrics acceptable (Lighthouse score > 90)
- [ ] No console errors or warnings

---

## 20. Conclusion

This design document provides a comprehensive blueprint for building SleepWise with a modern, dark, GenZ-friendly aesthetic. The design prioritizes:

1. **Visual Intelligence**: Data-driven insights presented beautifully
2. **Minimal Friction**: Clean, intuitive interfaces
3. **Hackathon Feasibility**: Achievable scope with modern tools
4. **Premium Feel**: Polished, professional appearance
5. **Accessibility**: Inclusive design for all users

The component-based architecture, Tailwind CSS styling, and Recharts integration ensure rapid development while maintaining high quality. Subtle animations and glassmorphism effects create a futuristic, AI-powered feel without overwhelming the user.

By following this design system, developers can build a cohesive, visually stunning application that stands out in the health-tech space and resonates with student users.

---

**Design Version**: 1.0  
**Last Updated**: 2026-02-24  
**Status**: Ready for Implementation
