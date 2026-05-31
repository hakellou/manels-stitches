from flask import Flask, render_template_string

app = Flask(__name__)

# رقم واتساب أختك (بالصيغة الدولية بدون أصفار، مثلاً: 213XXXXXXXXX)
WHATSAPP_NUMBER = "213552011543"  # 👈 ضع رقمها الحقيقي هنا

SERVICES = [
    {"id": 1, "name": "تفصيل فساتين مناسبات", "price": "تبدأ من 150 $", "image": "https://images.unsplash.com/photo-1566174053879-31528523f8ae?w=500", "description": "خياطة وتفصيل فساتين السهرة والمناسبات حسب المقاس والطلب بأجود أنواع الأقمشة."},
    {"id": 2, "name": "خياطة عبايات عصرية", "price": "تبدأ من 80 $", "image": "https://images.unsplash.com/photo-1583391733956-3750e0ff4e8b?w=500", "description": "عبايات أنيقة بتصميمات خليجية ومودرن تناسب الإطلالات اليومية والمناسبات."},
    {"id": 3, "name": "تعديل وإصلاح الملابس الاحترافي", "price": "حسب نوع التعديل", "image": "https://images.unsplash.com/photo-1528570188404-e826535188e7?w=500", "description": "تعديل المقاسات، تقصير، وإعادة تصميم الملابس القديمة لتناسب صيحات الموضة."},
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manel's Stitches | غرز منال للتميز</title>
    <style>
        :root { --primary-color: #ffb7b2; --dark-color: #2c3e50; }
        body { font-family: sans-serif; background-color: #fffafb; margin: 0; padding: 0; text-align: center; }
        navbar { display: flex; justify-content: space-between; align-items: center; background: white; padding: 15px 30px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        .logo-text { font-size: 24px; font-weight: bold; color: var(--dark-color); }
        .hero { background: linear-gradient(135deg, #ffe5ec 0%, #fff1f4 100%); padding: 40px 20px; }
        .container { max-width: 1100px; margin: 30px auto; display: flex; gap: 25px; justify-content: center; flex-wrap: wrap; }
        .card { background: white; border-radius: 12px; width: 300px; overflow: hidden; box-shadow: 0 6px 15px rgba(0,0,0,0.05); border-top: 4px solid var(--primary-color); text-align: right; }
        .card img { width: 100%; height: 220px; object-fit: cover; }
        .card-body { padding: 20px; }
        .price { color: #e91e63; font-size: 18px; font-weight: bold; margin: 15px 0 10px 0; }
        .btn { background: var(--dark-color); color: white; border: none; padding: 12px; width: 100%; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 15px; }
    </style>
</head>
<body>
    <navbar>
        <div class="logo-text">🪡 MANEL'S <span style="color: #e91e63;">STITCHES</span></div>
        <div style="font-size: 14px; color: #7f8c8d; font-weight: bold;">خياطة وتفصيل راقية ✨</div>
    </navbar>
    <div class="hero">
        <h1>مرحباً بكم في مشغل Manel's Stitches 🌸</h1>
        <p>تصفحي خدماتنا واطلبي تفصيلكِ الخاص الآن مباشرة عبر الواتساب.</p>
    </div>
    <div class="container">
        {% for service in services %}
        <div class="card">
            <img src="{{ service.image }}" alt="{{ service.name }}">
            <div class="card-body">
                <h3>{{ service.name }}</h3>
                <p style="font-size: 14px; color: #7f8c8d; line-height: 1.5;">{{ service.description }}</p>
                <div class="price">{{ service.price }}</div>
                <button class="btn" onclick="orderViaWhatsApp('{{ service.name }}')">طلب تفصيل وحجز الآن 💬</button>
            </div>
        </div>
        {% endfor %}
    </div>
    <script>
        function orderViaWhatsApp(serviceName) {
            let whatsappNumber = "{{ whatsapp_number }}";
            let message = encodeURIComponent("مرحباً مشغل Manel's Stitches، أود طلب تفصيل واستفسار لخدمة: (" + serviceName + ").");
            window.open("https://wa.me/" + whatsappNumber + "?text=" + message, '_blank');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, services=SERVICES, whatsapp_number=WHATSAPP_NUMBER)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)