from flask import Flask, render_template_string

app = Flask(__name__)

# رقم واتساب أختك منال الحقيقي بالصيغة الدولية للجزائر
WHATSAPP_NUMBER = "213552011543"

# قائمة المنتجات الحقيقية بروابط الصور المباشرة الجديدة التي أرسلتها
SERVICES = [
    {
        "id": 1, 
        "name": "فستان قطيفة أزرق ملكي مطرز بالخرز واللؤلؤ", 
        "price": "حسب نوع القماش والتطريز", 
        "image": "https://i.ibb.co/sdSjKmgR/1.jpg", 
        "description": "تصميم ساحر لفستان قطيفة بلون أزرق ملكي مع تفاصيل ورود بارزة، ومزين بطوق فاخر من اللؤلؤ والأحجار الكريمة على الصدر والرقبة."
    },
    {
        "id": 2, 
        "name": "مئزر (طابليّة) مطبخ بنقوش الورد والدانتيل", 
        "price": "حسب الموديل والطلب", 
        "image": "https://i.ibb.co/27Q0r8JM/2.jpg", 
        "description": "مئزر مطبخ أنيق جداً بلون بنفسجي (عنابي) دافئ، مدمج مع قماش بنقوش ورود ناعمة ومزين بلمسات الدانتيل الأبيض مع جيب عملي."
    },
    {
        "id": 3, 
        "name": "طقم أفرشة النزهات والوسائد (Picnic Set) الوردي", 
        "price": "حسب المقاس المطلوب", 
        "image": "https://i.ibb.co/kVZxHRzH/3.jpg", 
        "description": "بساط نزهات مبهج بنقوش مربعات وردية (Vichy) تأتي مع وسائد مريحة ومنتفخة بلون وردي فاقع مزينة بكرات البرودير البيضاء."
    },
    {
        "id": 4, 
        "name": "فستان قطيفة عنابي (سواري) مرصع بالأحجار", 
        "price": "حسب التطريز المطلوب", 
        "image": "https://i.ibb.co/hxQSFcVY/4.jpg", 
        "description": "فستان سهرة مخملي (قطيفة) باللون العنابي الملكي الفاخر، يتميز بقصة صدر أنيقة محددة بشريط برّاق من الكريستال والأحجار اللامعة."
    },
    {
        "id": 5, 
        "name": "فستان أطفال شتوي أخضر ملكي بياقة كلاسيكية", 
        "price": "أسعار مناسبة ومنافسة", 
        "image": "https://i.ibb.co/zVs8r3z1/5.jpg", 
        "description": "فستان بناتي ناعم باللون الأخضر الباستيل، مصمم بياقة بيضاء عريضة مطرزة بالدانتيل وتفاصيل دقيقة على الأكمام ليعطي مظهراً كلاسيكياً أنيقاً."
    },
    {
        "id": 6, 
        "name": "طقم بناتي جاكيت تويد وتنورة تول حمراء", 
        "price": "حسب عمر الطفلة", 
        "image": "https://i.ibb.co/jPqQwcNq/6.jpg", 
        "description": "طقم شتوي فاخر للأطفال يتكون من سترة (جاكيت) من قماش التويد الكلاسيكي المنسوج بنقوش حمراء وبيضاء مزين بوردة، مع تنورة تول حمراء منفوشة."
    },
    {
        "id": 7, 
        "name": "جبة تقليدية ملونة (ستايل قبائلي مطور)", 
        "price": "حسب التصميم والطلب", 
        "image": "https://i.ibb.co/0p50bLYh/7.jpg", 
        "description": "جبة تقليدية باللون الأصفر الساطع، تتميز بتطريز قبائلي كثيف ومميز بالألوان (الأحمر، الأخضر، الأسود) على الصدر والأكمام مع أكسسوارات متناسقة."
    },
    {
        "id": 8, 
        "name": "فستان أطفال صيفي بنقوش الورد والكروشيه", 
        "price": "أسعار مناسبة", 
        "image": "https://i.ibb.co/27PbtSXj/8.jpg", 
        "description": "فستان قطني ناعم للأطفال مزين بنقوش الورود الوردية الصغيرة، مع حزام عريض من الكروشيه الأبيض المشغول يدوياً بورود بارزة خضراء ووردية."
    },
    {
        "id": 9, 
        "name": "عباءة أو فستان استقبال وردي بالدانتيل الذهبي", 
        "price": "حسب نوع القماش", 
        "image": "https://i.ibb.co/Qv7mkM2C/9.jpg", 
        "description": "فستان استقبال أو مناسبات بلون وردي غامق (فوشيا) مصنوع من قماش منساب ومريح، ومزين بأشرطة عريضة من الدانتيل الذهبي المطرز بدقة على الصدر."
    }
]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>متجر Manel's Stitches | للأناقة عنوان</title>
    <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        :root { 
            --primary-bg: #fffafb; 
            --accent-pink: #ffb7b2; 
            --text-dark: #2c3e50; 
            --hot-pink: #e91e63; 
        }
        
        body { 
            font-family: 'Cairo', sans-serif; 
            background-color: var(--primary-bg); 
            margin: 0; 
            padding: 0; 
            text-align: center; 
            color: var(--text-dark);
        }
        
        navbar { 
            display: flex; 
            flex-direction: column;
            align-items: center; 
            background: white; 
            padding: 25px; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.04); 
            position: sticky; 
            top: 0; 
            z-index: 1000; 
        }
        
        .logo-text { 
            font-size: 30px; 
            font-weight: 900; 
            color: var(--text-dark); 
            letter-spacing: 1px;
            margin: 5px 0;
        }
        
        .tagline {
            font-size: 14px; 
            color: #7f8c8d; 
            font-weight: 700; 
            background: #fff0f3; 
            padding: 5px 15px; 
            border-radius: 20px;
            margin-top: 5px;
        }
        
        .hero { 
            background: linear-gradient(135deg, #ffe5ec 0%, #fff1f4 100%); 
            padding: 50px 20px; 
            border-bottom: 3px solid var(--accent-pink);
        }
        
        .hero h1 { margin: 0 0 15px 0; color: var(--text-dark); font-size: 34px; font-weight: 900; }
        .hero p { margin: 0; color: #555; font-size: 18px; font-weight: 600; }
        
        .section-title { margin: 40px 0 10px 0; color: var(--text-dark); font-size: 28px; font-weight: 700; position: relative; display: inline-block; }
        .section-title::after { content: ''; width: 60%; height: 4px; background: var(--hot-pink); position: absolute; bottom: -8px; left: 20%; border-radius: 2px; }
        
        .container { max-width: 1200px; margin: 30px auto; display: flex; gap: 30px; justify-content: center; flex-wrap: wrap; padding: 0 20px; }
        
        .card { 
            background: white; 
            border-radius: 20px; 
            width: 340px; 
            overflow: hidden; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.05); 
            border-top: 6px solid var(--accent-pink); 
            transition: all 0.3s ease; 
            display: flex; 
            flex-direction: column; 
            cursor: pointer;
        }
        .card:hover { transform: translateY(-8px); box-shadow: 0 15px 35px rgba(233, 30, 99, 0.15); }
        .card img { width: 100%; height: 340px; object-fit: cover; }
        
        .card-body { padding: 22px; text-align: right; display: flex; flex-direction: column; flex-grow: 1; }
        .card-body h3 { margin: 0 0 10px 0; color: var(--text-dark); font-size: 18px; font-weight: 700; line-height: 1.4; }
        .card-body p { font-size: 14px; color: #7f8c8d; line-height: 1.6; margin: 0 0 20px 0; flex-grow: 1; }
        
        .price { color: var(--hot-pink); font-size: 14px; font-weight: 700; margin-bottom: 15px; background: #fff0f3; padding: 6px 14px; border-radius: 20px; display: inline-block; width: fit-content; }
        
        .btn { background: var(--text-dark); color: white; border: none; padding: 14px; width: 100%; border-radius: 10px; cursor: pointer; font-weight: 700; font-size: 16px; transition: all 0.2s ease; display: flex; justify-content: center; align-items: center; gap: 8px; }
        .btn:hover { background: var(--hot-pink); box-shadow: 0 5px 15px rgba(233, 30, 99, 0.3); }
        
        .modal { display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.6); z-index: 2000; justify-content: center; align-items: center; backdrop-filter: blur(4px); }
        .modal-content { background: white; padding: 30px; border-radius: 24px; width: 90%; max-width: 450px; text-align: right; box-shadow: 0 20px 50px rgba(0,0,0,0.2); border-top: 8px solid var(--hot-pink); animation: fadeIn 0.3s ease; }
        @keyframes fadeIn { from { transform: translateY(20px); opacity: 0; } to { transform: translateY(0); opacity: 1; } }
        
        .modal h2 { margin-top: 0; color: var(--text-dark); font-size: 22px; font-weight: 700; border-bottom: 2px solid #eee; padding-bottom: 10px; }
        .modal-label { font-weight: 700; margin: 15px 0 5px 0; display: block; color: #555; }
        
        .select-input { width: 100%; padding: 12px; border-radius: 10px; border: 2px solid #e0e0e0; font-family: 'Cairo', sans-serif; font-size: 15px; background: #fafafa; outline: none; transition: border 0.2s; }
        .select-input:focus { border-color: var(--hot-pink); }
        
        .modal-buttons { display: flex; gap: 15px; margin-top: 25px; }
        .btn-confirm { background: #2ecc71; color: white; flex: 2; }
        .btn-confirm:hover { background: #27ae60; }
        .btn-cancel { background: #e74c3c; color: white; flex: 1; }
        .btn-cancel:hover { background: #c0392b; }
        
        footer { background: white; padding: 25px; margin-top: 50px; color: #7f8c8d; font-size: 14px; font-weight: 600; border-top: 2px solid #ffe5ec; }
    </style>
</head>
<body>

    <navbar>
        <div class="logo-text">🪡 MATJAR <span style="color: var(--hot-pink);">MANEL'S STITCHES</span></div>
        <div class="tagline">نُفصّل أحلامكِ غرزة بغرزة ✨</div>
    </navbar>
    
    <div class="hero">
        <h1>مرحباً بكم في متجر Manel's Stitches 🌸</h1>
        <p>تصفحي تصاميمنا الحقيقية، اختاري مقاسكِ ولونكِ المفضل واطلبي تفصيلك المخصص فوراً!</p>
    </div>
    
    <h2 class="section-title">كتالوج التصاميم والطلبات المخصصة</h2>
    
    <div class="container">
        {% for service in services %}
        <div class="card" onclick="openOrderModal('{{ service.name }}')">
            <img src="{{ service.image }}" alt="{{ service.name }}" onerror="this.src='https://placehold.co/600x400?text=Manel%27s+Stitches'">
            <div class="card-body">
                <h3>{{ service.name }}</h3>
                <p>{{ service.description }}</p>
                <div>
                    <div class="price">💎 {{ service.price }}</div>
                </div>
                <button class="btn">
                    <span>تخصيص وطلب الموديل</span> 💬
                </button>
            </div>
        </div>
        {% endfor %}
    </div>

    <div id="orderModal" class="modal">
        <div class="modal-content">
            <h2 id="modalTitle">تخصيص الطلب</h2>
            
            <label class="modal-label">📏 اختر المقاس المناسب لكِ:</label>
            <select id="sizeSelect" class="select-input">
                <option value="S (صغير)">S (صغير)</option>
                <option value="M (متوسط)">M (متوسط)</option>
                <option value="L (كبير)">L (كبير)</option>
                <option value="XL (كبير جداً)">XL (كبير جداً)</option>
                <option value="XXL (كبير مضاعف)">XXL (كبير مضاعف)</option>
                <option value="مقاس مخصص (سأرسل الأبعاد لاحقاً)">مقاس مخصص (سأرسل الأبعاد لاحقاً)</option>
            </select>
            
            <label class="modal-label">🎨 اختر اللون المفضل:</label>
            <select id="colorSelect" class="select-input">
                <option value="نفس لون الصورة الحقيقية">نفس لون الصورة المعروضة</option>
                <option value="أحمر ملكي">أحمر ملكي</option>
                <option value="وردي ناعم">وردي ناعم</option>
                <option value="أزرق ملكي">أزرق ملكي</option>
                <option value="أسود فاخر">أسود فاخر</option>
                <option value="أخضر زمردي">أخضر زمردي</option>
                <option value="لون مخصص آخر">لون مخصص آخر</option>
            </select>
            
            <div class="modal-buttons">
                <button class="btn btn-confirm" onclick="sendOrder()">تأكيد وإرسال عبر واتساب 🚀</button>
                <button class="btn btn-cancel" onclick="closeOrderModal()">إلغاء</button>
            </div>
        </div>
    </div>

    <footer>
        <p>© جميع الحقوق محفوظة لمتجر Manel's Stitches | صُنع وإبداع بكل فخر 💖</p>
    </footer>

    <script>
        let selectedProduct = "";

        function openOrderModal(productName) {
            selectedProduct = productName;
            document.getElementById('modalTitle').innerText = "تخصيص: " + productName;
            document.getElementById('orderModal').style.display = 'flex';
        }

        function closeOrderModal() {
            document.getElementById('orderModal').style.display = 'none';
        }

        function sendOrder() {
            let whatsappNumber = "{{ whatsapp_number }}";
            let size = document.getElementById('sizeSelect').value;
            let color = document.getElementById('colorSelect').value;
            
            let textMessage = "مرحباً متجر Manel's Stitches ✨\\n\\n" +
                              "أود طلب تفصيل الموديل التالي من موقعكم:\\n" +
                              "👗 الموديل: " + selectedProduct + "\\n" +
                              "📏 المقاس المختار: " + size + "\\n" +
                              "🎨 اللون المفضل: " + color + "\\n\\n" +
                              "فضلاً، هل الموديل متاح لبدء التفصيل وكم السعر والمدة المستغرقة؟";
                              
            let encodedMessage = encodeURIComponent(textMessage);
            window.open("https://wa.me/" + whatsappNumber + "?text=" + encodedMessage, '_blank');
            closeOrderModal();
        }
        
        window.onclick = function(event) {
            let modal = document.getElementById('orderModal');
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, services=SERVICES, whatsapp_number=WHATSAPP_NUMBER)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)