
document.addEventListener('DOMContentLoaded', () => {
  const forms = document.querySelectorAll('.add-to-bag-form');

  forms.forEach(form => {
    form.addEventListener('submit', function (e) {
      e.preventDefault();

      const formData = new FormData(form);
      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      fetch(form.action, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
          'X-Requested-With': 'XMLHttpRequest',
        },
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);     
        const totalElement = document.querySelector('#bag-total');
        if (totalElement && data.grand_total) {
          totalElement.textContent = `£${data.grand_total}`;
        }
      })
      .catch(error => {
        console.error('Error:', error);
      });
    });
  });
});

