document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert-dismissible');
  alerts.forEach(alertEl => {
    setTimeout(() => {
      try {
        const bsAlert = bootstrap.Alert.getOrCreateInstance(alertEl);
        bsAlert.close();
      } catch (e) {
        alertEl.remove();
      }
    }, 3000);
  });
});
// mark that the auto-dismiss logic is present
window.__alerts_auto_dismiss = true;
