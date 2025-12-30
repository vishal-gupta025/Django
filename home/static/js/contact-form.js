document.addEventListener('DOMContentLoaded', function () {
  const form = document.querySelector('form');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    const subject = form.querySelector('[name="subject"]').value.trim();
    const message = form.querySelector('[name="message"]').value.trim();

    let valid = true;
    form.querySelectorAll('.invalid-feedback').forEach(n => n.remove());

    function showError(el, text) {
      const div = document.createElement('div');
      div.className = 'invalid-feedback d-block small';
      div.textContent = text;
      el.parentNode.appendChild(div);
      valid = false;
    }

    if (!subject) showError(form.querySelector('[name="subject"]'), 'Please enter a subject');
    if (!message) showError(form.querySelector('[name="message"]'), 'Please enter a message');

    if (!valid) {
      e.preventDefault();
      return false;
    }

    const btn = form.querySelector('button[type="submit"]');
    if (btn) {
      btn.disabled = true;
      btn.innerHTML = 'Sending...';
    }
  });
});
