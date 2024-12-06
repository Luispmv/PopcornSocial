function openModal(movieId, movieTitle, movieDescription, posterUrl) {
    document.getElementById('modalTitle').textContent = movieTitle;
    document.getElementById('modalDescription').textContent = movieDescription;
    document.getElementById('modalPoster').src = posterUrl;

    // Asegúrate de que movieId sea válido
    document.getElementById('reviewButton').href = `/reviews/add/${movieId}/`;

    // Muestra el modal
    document.getElementById('movieModal').classList.remove('hidden');
}
