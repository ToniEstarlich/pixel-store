
/* Toast desyng */
function showToast(message, imageUrl) {
    const container = document.getElementById("toast-container");

    const toast = document.createElement("div");
    toast.classList.add("toast-item");

    toast.innerHTML = `
        <div style="display: flex; align-items: center;">
            <img src="${imageUrl}" alt="Product" style="width:50px; height:50px; object-fit:cover; border-radius:5px; margin-right:10px;">
            <span>${message}</span>
        </div>
    `;

    container.appendChild(toast);

    // Fade in
    toast.style.opacity = "0";
    toast.style.transition = "opacity 0.5s ease, transform 0.5s ease";
    setTimeout(() => toast.style.opacity = "1", 100);

    // Fade out y remover
    setTimeout(() => {
        toast.style.opacity = "0";
        setTimeout(() => toast.remove(), 3000);
    }, 3000);
}

// call of endpoint add_to_bag

document.querySelectorAll(".add-to-bag-form").forEach(form => {
    form.addEventListener("submit", function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        const url = this.action;

        fetch(url, {
            method: "POST",
            body: formData,
            headers: {
                "X-CSRFToken": formData.get("csrfmiddlewaretoken")
            }
        })
        .then(response => response.json())
        .then(data => {
            showToast( `${data.product_name} added to your bag!`, data.image_url);
        })
        .catch(error => {
            console.error("Error:",error)
        });
    });

});