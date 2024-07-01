document.getElementById('create-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const roll_number = document.getElementById('student-roll-number').value;
    const name = document.getElementById('student-name').value;
    const dob = document.getElementById('student-dob').value;
    const class_ = document.getElementById('student-class').value;
    const section = document.getElementById('student-section').value;
    const class_teacher = document.getElementById('student-class-teacher').value;
    const fee = document.getElementById('student-fee').value;
    const active = document.getElementById('student-active').checked;

    const response = await fetch('/students', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ roll_number, name, dob, class: class_, section, class_teacher, fee, active })
    });
    const data = await response.json();
    alert(data.message);
});

document.getElementById('get-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const studentId = document.getElementById('get-student-id').value;

    const response = await fetch(`/students/${studentId}`);
    const data = await response.json();
    document.getElementById('student-info').textContent = JSON.stringify(data, null, 2);
});

document.getElementById('get-all-students').addEventListener('click', async () => {
    const response = await fetch('/students');
    const data = await response.json();
    document.getElementById('all-students-info').textContent = JSON.stringify(data, null, 2);
});

document.getElementById('update-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const studentId = document.getElementById('update-student-id').value;
    const roll_number = document.getElementById('update-student-roll-number').value;
    const name = document.getElementById('update-student-name').value;
    const dob = document.getElementById('update-student-dob').value;
    const class_ = document.getElementById('update-student-class').value;
    const section = document.getElementById('update-student-section').value;
    const class_teacher = document.getElementById('update-student-class-teacher').value;
    const fee = document.getElementById('update-student-fee').value;
    const active = document.getElementById('update-student-active').checked;

    const response = await fetch(`/students/${studentId}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ roll_number, name, dob, class: class_, section, class_teacher, fee, active })
    });
    const data = await response.json();
    alert(data.message);
});

document.getElementById('delete-student-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const studentId = document.getElementById('delete-student-id').value;

    const response = await fetch(`/students/${studentId}`, {
        method: 'DELETE'
    });
    const data = await response.json();
    alert(data.message);
});

document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    const response = await fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    });
    const data = await response.json();
    document.getElementById('login-message').textContent = data.message;
});