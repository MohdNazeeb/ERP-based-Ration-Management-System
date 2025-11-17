// ✅ CAPTCHA GENERATOR
function generateCaptcha(id) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let captcha = '';
  for (let i = 0; i < 5; i++) {
    captcha += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  document.getElementById(id).textContent = captcha;
}

// ✅ Preview Image Function
function previewImage(inputId, previewId) {
  const input = document.getElementById(inputId);
  const preview = document.getElementById(previewId);
  if (!input) return;
  input.addEventListener('change', function () {
    const file = this.files[0];
    if (file && file.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = e => {
        preview.src = e.target.result;
        preview.style.display = 'block';
      };
      reader.readAsDataURL(file);
    } else {
      preview.style.display = 'none';
    }
  });
}

// ✅ Distributor OTP Simulation
function sendDistributorOTP() {
  const otp = Math.floor(100000 + Math.random() * 900000);
  alert(`Your Distributor OTP is: ${otp}`);
}

// ✅ Load shared header and footer
document.addEventListener("DOMContentLoaded", () => {
  const includeElements = document.querySelectorAll("[data-include]");
  includeElements.forEach(el => {
    fetch(el.getAttribute("data-include"))
      .then(resp => resp.text())
      .then(html => el.innerHTML = html);
  });
});
