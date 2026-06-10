"""
Create PDF versions of Sheet A and Sheet B
Each PDF is exactly 1 page
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_sheet_a_pdf():
    """Create Sheet A PDF - Unorganized version"""

    filename = "Sheet_A_Unorganized.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            topMargin=0.3*inch, bottomMargin=0.3*inch,
                            leftMargin=0.4*inch, rightMargin=0.4*inch)

    # Styles
    styles = getSampleStyleSheet()

    # Custom styles for compact layout
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=6,
        alignment=TA_CENTER,
        bold=True
    )

    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=10,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=4,
        spaceBefore=6,
        bold=True
    )

    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontSize=8,
        leading=10,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=7,
        leading=8.5,
        spaceAfter=2,
        alignment=TA_LEFT
    )

    # Content
    story = []

    # Title
    story.append(Paragraph("College Tech Fest 2024 - Event Information", title_style))
    story.append(Spacer(1, 0.05*inch))

    # Instructions
    story.append(Paragraph("<b>ANSWER THESE 10 QUESTIONS</b> (You have 3 minutes):", heading_style))
    story.append(Spacer(1, 0.05*inch))

    # Questions
    questions = [
        "1. Which event offers the best value if you're a student interested in both learning AND winning money? ______________",
        "2. If you want to attend all free events that teach security-related topics, which dates must you block? ______________",
        "3. A student has ₹300 budget. Which paid events can they attend and how much will be left? ______________",
        "4. Which events have speakers from companies (not academia)? Name all. ______________",
        "5. If two events happen on March 12, which one requires you to bring your own laptop with specific software? ______________",
        "6. What's the TOTAL time commitment (in hours) if you attend both the AI Workshop (all days) and Data Science Symposium? ______________",
        "7. Which event gives you access to datasets AND course materials? ______________",
        "8. If you can only attend events in Block C or Main Auditorium, which events are possible? ______________",
        "9. Which event has the strictest capacity limit? ______________",
        "10. Name the event where you can earn something beyond certificates (other than prize money). ______________"
    ]

    for q in questions:
        story.append(Paragraph(q, question_style))

    story.append(Spacer(1, 0.1*inch))

    # Event Information
    story.append(Paragraph("<b>Event Information</b> (Read carefully to find answers)", heading_style))
    story.append(Spacer(1, 0.05*inch))

    # Full text in one paragraph with line breaks
    event_text = """
Our annual tech fest is back and bigger than ever with exciting opportunities for all students to learn and compete. The fest will run from March 10-17, 2024 across various venues in the campus. We have partnered with leading tech companies to bring you industry experts and amazing prizes worth over ₹5 lakhs in total. Students from all years and departments are welcome to participate.
<br/><br/>
The <b>Coding Marathon</b>, which has been our flagship event for three years, will test your algorithmic thinking and problem-solving speed. This year's marathon will be held on March 16 in the Computer Lab, Building A, starting at 9 AM sharp. The competition will run for 6 hours continuously with breaks allowed. Winners will receive exciting prizes - first prize is ₹50,000 cash prize plus an internship opportunity at TechCorp, one of India's leading software companies, second prize is ₹30,000 and third prize is ₹15,000. All participants will receive participation certificates and refreshments throughout the event. No registration fee required - completely free to participate for all students.
<br/><br/>
The fest also features several workshops designed to upskill students in emerging technologies. The <b>Cybersecurity Bootcamp</b> is a 2-day intensive workshop scheduled for March 12-13 where participants will learn about ethical hacking, penetration testing, and security best practices. The bootcamp will be conducted in the Main Auditorium, Block C, and is completely free for all registered students. Industry expert Mr. Anand Sharma from CyberDefense Inc. will lead the sessions. Participants need to bring their laptops with Kali Linux pre-installed. The workshop will cover topics like network security, web application security, and malware analysis. Limited seats available - only 100 students can register, so register early to avoid disappointment.
<br/><br/>
For those interested in AI and machine learning, we have the <b>AI Workshop</b> running parallel to other events. This workshop will dive deep into neural networks, deep learning frameworks like TensorFlow and PyTorch, and practical applications of AI in real-world scenarios. The workshop fee structure is designed to be affordable - ₹400 for general participants and ₹250 for students who show their valid college ID card. The workshop spans 3 days from March 10-12, with sessions from 2 PM to 6 PM daily in the IT Department Seminar Hall. That's a total of 12 hours of learning time. Registration closes on March 15, 2024 at 11:59 PM, so make sure you sign up before the deadline. The workshop will include hands-on projects where students will build their own AI models from scratch.
<br/><br/>
We're also hosting a <b>Data Science Symposium</b> on March 14, featuring talks from data scientists working at Fortune 500 companies. The symposium will cover topics ranging from data preprocessing, feature engineering, machine learning models, to deployment strategies. Guest speakers include Ms. Priya Desai from Google and Mr. Vikram Reddy from Microsoft - both are industry professionals currently working at these companies. The registration fee is ₹500, but students can avail a special discount - just ₹300 if they present their college ID at the registration desk. The event will take place in the Convention Center from 10 AM to 5 PM with lunch provided, totaling 7 hours. Attendees will receive exclusive access to course materials and datasets used during the presentations.
<br/><br/>
Last but not least, we have the <b>Blockchain Seminar</b> scheduled for March 17, the closing day of the fest. Blockchain technology is revolutionizing industries from finance to healthcare, and this seminar will provide foundational knowledge about distributed ledger technology, smart contracts, and cryptocurrency basics. The keynote speaker is Dr. Rajesh Kumar, a renowned blockchain researcher from IIT Delhi who has published over 50 papers in international journals and has worked with multiple blockchain startups. Dr. Kumar is an academic researcher, not an industry professional. The seminar is free to attend but requires prior registration due to limited seating capacity of 150 participants. Venue is the Main Lecture Hall, and the session runs from 11 AM to 2 PM with a Q&A session at the end, making it a 3-hour commitment.
<br/><br/>
Student volunteers are also needed for various events - if you're interested in volunteering, you can earn <b>community service credits</b> which count toward your degree requirements. All registrations must be done online through our fest portal at www.collegetechfest2024.edu. Payment can be made via UPI, credit/debit card, or net banking. For any queries, contact the organizing committee at techfest2024@college.edu or call +91-9876543210. Don't miss this incredible opportunity to learn, network, and showcase your skills. Mark your calendars and we'll see you at the fest!
"""

    story.append(Paragraph(event_text, body_style))

    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph("<b>TIME'S UP! Now flip the paper and try the same questions again.</b>", heading_style))

    # Build PDF
    doc.build(story)
    print(f"[+] Created {filename}")


def create_sheet_b_pdf():
    """Create Sheet B PDF - Organized version"""

    filename = "Sheet_B_Chunked.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4,
                            topMargin=0.3*inch, bottomMargin=0.3*inch,
                            leftMargin=0.4*inch, rightMargin=0.4*inch)

    # Styles
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=13,
        textColor=colors.HexColor('#1a1a1a'),
        spaceAfter=4,
        alignment=TA_CENTER,
        bold=True
    )

    event_title_style = ParagraphStyle(
        'EventTitle',
        parent=styles['Heading2'],
        fontSize=9,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=2,
        spaceBefore=3,
        bold=True
    )

    question_style = ParagraphStyle(
        'QuestionStyle',
        parent=styles['Normal'],
        fontSize=7.5,
        leading=9,
        spaceAfter=2
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=6.5,
        leading=7.5,
        spaceAfter=1
    )

    # Content
    story = []

    # Title
    story.append(Paragraph("College Tech Fest 2024 - Event Information (Organized)", title_style))
    story.append(Spacer(1, 0.03*inch))

    # Instructions
    story.append(Paragraph("<b>ANSWER THESE 10 QUESTIONS</b> (You have 2 minutes):", event_title_style))

    # Questions (compact)
    questions = [
        "1. Which event offers best value for student learning + winning? ____",
        "2. Free security events - which dates? ____",
        "3. ₹300 budget - which paid events + leftover? ____",
        "4. Company speakers (not academia)? ____",
        "5. March 12 - which needs laptop with software? ____",
        "6. Total hours: AI Workshop (all days) + Data Science? ____",
        "7. Which gives datasets AND materials? ____",
        "8. Only Block C or Main Auditorium - which events? ____",
        "9. Strictest capacity limit? ____",
        "10. Earn beyond certificates (not prize money)? ____"
    ]

    for q in questions:
        story.append(Paragraph(q, question_style))

    story.append(Spacer(1, 0.05*inch))

    # Event catalog
    story.append(Paragraph("<b>📋 Event Catalog</b>", event_title_style))

    # Event 1: Coding Marathon
    story.append(Paragraph("<b>EVENT 1: Coding Marathon</b>", body_style))
    story.append(Paragraph("📅 Mar 16, 9AM-3PM (6hrs) | 📍 Computer Lab, Bldg A | 💰 FREE | 🏆 ₹50K+internship, ₹30K, ₹15K | 🎓 Algo thinking, problem solving | ✅ Unlimited capacity", body_style))

    # Event 2: Cybersecurity Bootcamp
    story.append(Paragraph("<b>EVENT 2: Cybersecurity Bootcamp</b>", body_style))
    story.append(Paragraph("📅 Mar 12-13 (2 days) | 📍 Main Auditorium, Block C | 💰 FREE | 👨‍🏫 Anand Sharma (CyberDefense Inc. - Industry) | 🎓 Ethical hacking, pentesting, network/web security | 💻 NEED: Laptop with Kali Linux | 👥 100 capacity", body_style))

    # Event 3: AI Workshop
    story.append(Paragraph("<b>EVENT 3: AI Workshop</b>", body_style))
    story.append(Paragraph("📅 Mar 10-12 (3 days), 2-6PM (12hrs total) | 📍 IT Dept Seminar Hall | 💰 ₹250 (students) | 🎓 Neural networks, TensorFlow, PyTorch, hands-on AI models | 📝 Reg deadline: Mar 15", body_style))

    # Event 4: Data Science Symposium
    story.append(Paragraph("<b>EVENT 4: Data Science Symposium</b>", body_style))
    story.append(Paragraph("📅 Mar 14, 10AM-5PM (7hrs) | 📍 Convention Center | 💰 ₹300 (students) | 👥 Priya Desai (Google), Vikram Reddy (Microsoft) - Industry | 🎓 Data preprocessing, feature eng, ML, deployment | 🎁 Lunch + Course materials + Datasets", body_style))

    # Event 5: Blockchain Seminar
    story.append(Paragraph("<b>EVENT 5: Blockchain Seminar</b>", body_style))
    story.append(Paragraph("📅 Mar 17, 11AM-2PM (3hrs) | 📍 Main Lecture Hall | 💰 FREE | 👨‍🏫 Dr. Rajesh Kumar (IIT Delhi - Academia) 50+ papers | 🎓 DLT, smart contracts, crypto | 👥 150 capacity", body_style))

    story.append(Spacer(1, 0.05*inch))

    # Quick reference tables
    story.append(Paragraph("<b>🎯 Quick Reference</b>", event_title_style))

    # Price table
    price_data = [
        ['Event', 'Student Fee'],
        ['Coding Marathon', 'FREE'],
        ['Cybersecurity', 'FREE'],
        ['Blockchain', 'FREE'],
        ['AI Workshop', '₹250'],
        ['Data Science', '₹300']
    ]

    price_table = Table(price_data, colWidths=[2*inch, 1*inch])
    price_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(price_table)

    story.append(Spacer(1, 0.05*inch))

    # Venue table
    venue_data = [
        ['Venue', 'Events'],
        ['Main Aud, Block C', 'Cybersecurity'],
        ['Computer Lab, Bldg A', 'Coding Marathon'],
        ['IT Seminar Hall', 'AI Workshop'],
        ['Convention Center', 'Data Science'],
        ['Main Lecture Hall', 'Blockchain']
    ]

    venue_table = Table(venue_data, colWidths=[1.8*inch, 1.8*inch])
    venue_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 3),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey)
    ]))
    story.append(venue_table)

    story.append(Spacer(1, 0.04*inch))

    # Speaker types
    story.append(Paragraph("<b>👥 Speaker Types:</b> Industry: Anand Sharma, Priya Desai, Vikram Reddy | Academia: Dr. Rajesh Kumar", body_style))
    story.append(Paragraph("<b>🎁 Special:</b> Prize Money + Internship (Coding) | Materials + Datasets (Data Science) | Community Credits (Volunteering)", body_style))

    story.append(Spacer(1, 0.04*inch))
    story.append(Paragraph("📞 www.collegetechfest2024.edu | techfest2024@college.edu | +91-9876543210", body_style))

    story.append(Spacer(1, 0.04*inch))
    story.append(Paragraph("<b>Much easier, right? That's RAG! Organization + Metadata = Fast, accurate retrieval. 🚀</b>", event_title_style))

    # Build PDF
    doc.build(story)
    print(f"[+] Created {filename}")


if __name__ == "__main__":
    import sys
    if sys.platform == 'win32':
        sys.stdout.reconfigure(encoding='utf-8')

    print("\n[*] Generating PDFs...")
    print("-" * 50)

    create_sheet_a_pdf()
    create_sheet_b_pdf()

    print("-" * 50)
    print("[+] Done! Both PDFs created in the current directory.")
    print("\nSheet_A_Unorganized.pdf - 1 page (unorganized)")
    print("Sheet_B_Chunked.pdf - 1 page (organized with metadata)")
    print("\nReady to print for your workshop!")
