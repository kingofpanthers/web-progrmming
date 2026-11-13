from django.http import HttpResponse


def home(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Management System</title>
    <style>
        * { box-sizing: border-box; }
        body { margin: 0; font-family: Arial, sans-serif; background: #f3f6fb; color: #243047; }
        header { background: #2449a4; color: white; padding: 28px 24px; }
        header div, main { max-width: 960px; margin: auto; }
        h1 { margin: 0 0 8px; font-size: 28px; }
        header p { margin: 0; color: #dce6ff; }
        main { padding: 28px 20px; }
        .card { background: white; border: 1px solid #dce3ef; border-radius: 12px; padding: 24px; margin-bottom: 24px; }
        h2 { margin: 0 0 12px; font-size: 21px; }
        p { line-height: 1.6; }
        .note { color: #59677d; font-size: 14px; }
        .table-wrap { overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; text-align: left; }
        th, td { padding: 15px 12px; border-bottom: 1px solid #e5eaf2; }
        th { background: #f4f7fc; font-size: 14px; }
        .status { background: #e5f6ed; color: #17623b; padding: 5px 10px; border-radius: 20px; font-size: 13px; }
        footer { text-align: center; color: #59677d; padding: 12px 20px 28px; font-size: 14px; }
    </style>
</head>
<body>
    <header>
        <div>
            <h1>Student Management System</h1>
            <p>A simple place to view student information.</p>
        </div>
    </header>
    <main>
        <section class="card" aria-labelledby="welcome-heading">
            <h2 id="welcome-heading">Welcome to your student dashboard</h2>
            <p>Keep student names, contact details, and courses organized in one place.</p>
            <p class="note">This is a sample page. The records below are demonstration data.</p>
        </section>
        <section class="card" aria-labelledby="students-heading">
            <h2 id="students-heading">Student list</h2>
            <div class="table-wrap">
                <table>
                    <caption class="note">Sample student records</caption>
                    <thead>
                        <tr><th scope="col">Student ID</th><th scope="col">Name</th><th scope="col">Email</th><th scope="col">Course</th><th scope="col">Status</th></tr>
                    </thead>
                    <tbody>
                        <tr><td>ST001</td><td>Amaya Perera</td><td>amaya@example.com</td><td>Computer Science</td><td><span class="status">Active</span></td></tr>
                        <tr><td>ST002</td><td>dafni Silva</td><td>dafni@example.com</td><td>Business Management</td><td><span class="status">Active</span></td></tr>
                        <tr><td>ST003</td><td>Nethmi Fernando</td><td>nethmi@example.com</td><td>Information Technology</td><td><span class="status">Active</span></td></tr>
                    </tbody>
                </table>
            </div>
        </section>
    </main>
    <footer>Student Management System</footer>
</body>
</html>""")
