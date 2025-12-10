import { useEffect, useState } from "react";
import { useAuth } from "../context/AuthContext";

interface Movie {
  id: number;
  title: string;
  genre: string;
  year: number;
}

function MovieList() {
  const { token } = useAuth();
  const [movies, setMovies] = useState<Movie[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const res = await fetch("http://127.0.0.1:8000/api/movies/", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });

        const data = await res.json();
        setMovies(data);
      } catch (err) {
        console.error("Error fetching movies:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchMovies();
  }, [token]);

  if (!token) {
    return <p>You must be logged in.</p>;
  }

  if (loading) {
    return <p>Loading movies...</p>;
  }

  return (
    <div style={{ maxWidth: 400, margin: "40px auto" }}>
      <h2>Your Movie List</h2>

      {movies.length === 0 && <p>No movies yet.</p>}

      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            <strong>{movie.title}</strong> ({movie.year}) — {movie.genre}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default MovieList;
