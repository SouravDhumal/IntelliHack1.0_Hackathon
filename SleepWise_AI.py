from flask import Flask, request, render_template_string

app = Flask(__name__)

# Store weekly scores in memory
weekly_data = {
    "Monday": 0,
    "Tuesday": 0,
    "Wednesday": 0,
    "Thursday": 0,
    "Friday": 0,
    "Saturday": 0,
    "Sunday": 0
}

def safe_float(x):
    try:
        return float(x)
    except:
        return 0.0

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        day = request.form.get("day")
        sleep = safe_float(request.form.get("sleep"))
        stress = safe_float(request.form.get("stress"))
        screen = safe_float(request.form.get("screen"))
        mood = safe_float(request.form.get("mood"))

        # ---- Sleep Score ----
        sleep_score = min(100, max(
            0,
            (sleep / 8) * 60 +
            mood * 8 -
            stress * 5 -
            screen * 2
        ))

        # ---- Burnout Probability ----
        burnout_prob = min(100, max(
            5,
            stress * 15 +
            screen * 5 -
            sleep * 6
        ))

        # ---- Burnout Hours ----
        burnout_hours = max(
            1.0,
            round(
                8
                - stress * 0.8
                - screen * 0.4
                + sleep * 0.3
                + mood * 0.4,
                1
            )
        )

        # ---- Dynamic Peak Hours ----
        if sleep >= 7 and stress <= 2:
            peak_hours = "7:30 AM – 11:00 AM"
        elif stress >= 4:
            peak_hours = "10:30 AM – 1:00 PM"
        else:
            peak_hours = "9:00 AM – 12:00 PM"

        # ---- Cognitive Stability Index ----
        stability = round((sleep_score - burnout_prob + mood * 10) / 2)

        # ---- Actionable Suggestions ----
        actionable = []

        if screen > 4:
            actionable.append("Set a strict 10:30 PM screen cut-off alarm.")
        if stress >= 4:
            actionable.append("Schedule a 15-min evening decompression walk.")
        if sleep < 6:
            actionable.append("Fix an 11:30 PM sleep deadline tonight.")
        if mood <= 2:
            actionable.append("Add one enjoyable activity before bed.")

        if not actionable:
            actionable.append("Maintain this routine and increase deep-work blocks during peak hours.")

        suggestion = " • ".join(actionable)

        # Save weekly score
        if day:
            weekly_data[day] = round(sleep_score)

        result = {
            "sleep_score": round(sleep_score),
            "burnout_prob": round(burnout_prob),
            "burnout_hours": burnout_hours,
            "peak_hours": peak_hours,
            "suggestion": suggestion,
            "stability": stability,
            "radar": [
                min(100, sleep * 12),
                100 - stress * 15,
                mood * 20,
                100 - screen * 10,
                burnout_prob
            ],
            "weekly": list(weekly_data.values())
        }

    return render_template_string(TEMPLATE, result=result)


TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
<title>SleepWise AI</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body{
    margin:0;
    font-family:'Inter',sans-serif;
    background:#0b0c0f;
    color:#e5e5e5;
}
.wrapper{
    max-width:1100px;
    margin:auto;
    padding:60px 40px 140px;
}
h1{
    font-size:70px;
    text-align:center;
    font-weight:800;
    margin-bottom:10px;
    background:linear-gradient(135deg,#6366f1,#8b5cf6);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}
.subtitle{
    text-align:center;
    color:#9ca3af;
    margin-bottom:60px;
}
.panel{
    background:#14161b;
    border-radius:26px;
    padding:55px;
    margin-bottom:60px;
    box-shadow:0 30px 90px rgba(0,0,0,0.85);
}
input, select{
    width:100%;
    padding:18px;
    font-size:16px;
    margin-bottom:18px;
    border-radius:14px;
    border:none;
    background:#1f2229;
    color:#fff;
}
button{
    width:100%;
    padding:18px;
    border:none;
    border-radius:16px;
    background:linear-gradient(135deg,#6366f1,#8b5cf6);
    color:#fff;
    font-size:17px;
    font-weight:600;
    cursor:pointer;
}
.section-title{
    font-size:30px;
    margin-bottom:20px;
}
.big-text{
    font-size:58px;
    font-weight:800;
}
.center{text-align:center;}
canvas{
    max-width:420px;
    margin:35px auto 0;
    display:block;
}
p{
    font-size:18px;
    line-height:1.75;
    color:#cbd5f5;
}
</style>
</head>

<body>
<div class="wrapper">

<h1>SleepWise AI</h1>
<p class="subtitle">Behavior-Driven Cognitive Analytics Engine</p>

<div class="panel">
<form method="POST">
    <select name="day" required>
        <option value="">Select Day</option>
        <option>Monday</option>
        <option>Tuesday</option>
        <option>Wednesday</option>
        <option>Thursday</option>
        <option>Friday</option>
        <option>Saturday</option>
        <option>Sunday</option>
    </select>

    <input name="sleep" placeholder="Sleep hours (e.g. 7)" required>
    <input name="stress" placeholder="Stress level (1–5)" required>
    <input name="screen" placeholder="Screen time (hours)" required>
    <input name="mood" placeholder="Mood (1–5)" required>
    <button>Analyze</button>
</form>
</div>

{% if result %}
<div class="panel center">
    <div class="section-title">Sleep Quality Score</div>
    <div class="big-text">{{result.sleep_score}} / 100</div>
    <canvas id="radar"></canvas>
</div>

<div class="panel center">
    <div class="section-title">Cognitive Stability Index</div>
    <div class="big-text">{{result.stability}} / 100</div>
</div>

<div class="panel">
    <div class="section-title">Peak Productivity Hours</div>
    <p>{{result.peak_hours}}</p>
</div>

<div class="panel">
    <div class="section-title">Predictive Burnout Window</div>
    <p>Mental fatigue likely after <strong>{{result.burnout_hours}} productive hours</strong>.</p>
</div>

<div class="panel">
    <div class="section-title">Burnout Probability</div>
    <p><strong>{{result.burnout_prob}}%</strong> likelihood if habits continue.</p>
</div>

<div class="panel">
    <div class="section-title">Action Plan</div>
    <p>{{result.suggestion}}</p>
</div>

<div class="panel center">
    <div class="section-title">Weekly Sleep Trend</div>
    <canvas id="weekly"></canvas>
</div>
{% endif %}

</div>

{% if result %}
<script>
new Chart(document.getElementById("radar"),{
    type:"radar",
    data:{
        labels:["Sleep","Stress","Mood","Screen","Burnout"],
        datasets:[{
            data: {{result.radar}},
            backgroundColor:"rgba(139,92,246,0.2)",
            borderColor:"#8b5cf6",
            pointBackgroundColor:"#fff"
        }]
    },
    options:{
        scales:{ r:{ min:0,max:100,ticks:{display:false} } },
        plugins:{legend:{display:false}}
    }
});

new Chart(document.getElementById("weekly"),{
    type:"bar",
    data:{
        labels:["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        datasets:[{
            data: {{result.weekly}},
            backgroundColor:"#6366f1"
        }]
    },
    options:{
        plugins:{legend:{display:false}},
        scales:{y:{min:0,max:100}}
    }
});
</script>
{% endif %}
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)