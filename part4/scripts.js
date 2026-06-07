const API_URL = 'http://127.0.0.1:5000/api/v1';

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
    return null;
}

document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');

    const loginLink = document.getElementById('login-link');
    const logoutButton = document.getElementById('logout-button');
    
    if (loginLink && logoutButton) {
        if (token) {
            loginLink.style.display = 'none';
            logoutButton.style.display = 'block';
        } else {
            loginLink.style.display = 'block';
            logoutButton.style.display = 'none';
        }

        logoutButton.addEventListener('click', () => {
            document.cookie = "token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
            window.location.href = 'index.html';
        });
    }

    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch(`${API_URL}/auth/login`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email, password })
                });

                if (response.ok) {
                    const data = await response.json();
                    document.cookie = `token=${data.access_token}; path=/`;
                    window.location.href = 'index.html';
                } else {
                    const errData = await response.json();
                    alert('Login failed: ' + (errData.msg || response.statusText));
                }
            } catch (error) {
                alert('API Connection error!');
            }
        });
    }

    const placesList = document.getElementById('places-list');
    if (placesList) {
        async function fetchPlaces() {
            try {
                const response = await fetch(`${API_URL}/places`);
                if (response.ok) {
                    const places = await response.json();
                    displayPlaces(places);
                }
            } catch (error) {
                console.error('Failed to fetch places:', error);
            }
        }

        function displayPlaces(places) {
            placesList.innerHTML = '';
            places.forEach(place => {
                const card = document.createElement('div');
                card.className = 'place-card';
                card.setAttribute('data-price', place.price);
                
                card.innerHTML = `
                    <h3>${place.title}</h3>
                    <p class="price">$${place.price} / night</p>
                    <a href="place.html?id=${place.id}" class="details-button">View Details</a>
                `;
                placesList.appendChild(card);
            });
        }

        const priceFilter = document.getElementById('price-filter');
        priceFilter.addEventListener('change', (event) => {
            const selectedValue = event.target.value;
            const cards = document.querySelectorAll('.place-card');

            cards.forEach(card => {
                const cardPrice = parseFloat(card.getAttribute('data-price'));
                if (selectedValue === 'All') {
                    card.style.display = 'block';
                } else {
                    const maxPrice = parseFloat(selectedValue);
                    if (cardPrice <= maxPrice) {
                        card.style.display = 'block';
                    } else {
                        card.style.display = 'none';
                    }
                }
            });
        });

        fetchPlaces();
    }

    const placeDetailsSection = document.getElementById('place-details');
    if (placeDetailsSection) {
        const urlParams = new URLSearchParams(window.location.search);
        const placeId = urlParams.get('id');

        if (!placeId) {
            window.location.href = 'index.html';
            return;
        }

        async function fetchPlaceDetails() {
            try {
                const response = await fetch(`${API_URL}/places/${placeId}`);
                if (response.ok) {
                    const place = await response.json();
                    displayPlaceDetails(place);
                }
            } catch (error) {
                console.error(error);
            }
        }

        function displayPlaceDetails(place) {
            let reviewsHTML = '<h3>Reviews</h3>';
            if (place.reviews && place.reviews.length > 0) {
                place.reviews.forEach(rev => {
                    reviewsHTML += `
                        <div class="review-card">
                            <p><strong>Rating:</strong> ${rev.rating}/5</p>
                            <p>${rev.text}</p>
                        </div>
                    `;
                });
            } else {
                reviewsHTML += '<p>No reviews yet for this place.</p>';
            }

            placeDetailsSection.innerHTML = `
                <h2>${place.title}</h2>
                <div class="place-info">
                    <p><strong>Description:</strong> ${place.description || 'No description provided.'}</p>
                    <p class="price"><strong>Price:</strong> $${place.price} / night</p>
                </div>
                <hr style="margin: 20px 0; border: 0; border-top: 1px solid #ddd;">
                <div class="reviews-section">
                    ${reviewsHTML}
                </div>
            `;
            const addReviewSection = document.getElementById('add-review');
            if (addReviewSection && token) {
                addReviewSection.style.display = 'block';
                document.getElementById('write-review-btn').addEventListener('click', () => {
                    window.location.href = `add_review.html?id=${place.id}`;
                });
            }
        }

        fetchPlaceDetails();
    }

    const reviewForm = document.getElementById('review-form');
    if (reviewForm) {
        const urlParams = new URLSearchParams(window.location.search);
        const placeId = urlParams.get('id');

        if (!token || !placeId) {
            window.location.href = 'index.html';
            return;
        }

        reviewForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            const rating = document.getElementById('review-rating').value;
            const text = document.getElementById('review-text').value;

            try {
                const response = await fetch(`${API_URL}/reviews`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Authorization': `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        place_id: placeId,
                        rating: parseInt(rating),
                        text: text
                    })
                });

                if (response.ok) {
                    alert('Review submitted successfully!');
                    window.location.href = `place.html?id=${placeId}`;
                } else {
                    alert('Failed to submit review. You might be the host or already reviewed.');
                }
            } catch (error) {
                alert('Error submitting review');
            }
        });
    }
});