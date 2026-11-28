
import './App.css'

function App() {
  return (
    <div className="app">
      <header className="topbar">
        <span>THE WORLD. IN FOCUS.</span>
        <span>YOUR DAILY NEWS DESTINATION</span>
      </header>

      <div className="masthead">
        <h1>THE DAILY<span>.</span></h1>
        <p>INDEPENDENT NEWS & JOURNALISM</p>
      </div>

      <nav className="navbar">
        <a href="#home">HOME</a>
        <a href="#technology">TECHNOLOGY</a>
        <a href="#business">BUSINESS</a>
        <a href="#science">SCIENCE</a>
        <a href="#sports">SPORTS</a>
      </nav>

      <div className="breaking">
        <strong>BREAKING</strong>
        <span>Stay informed. Stay ahead. Discover the stories shaping our world.</span>
      </div>

      <main className="content" id="home">
        <div className="section-heading">
          <span>THE EDITION</span>
          <span>YOUR WORLD, TODAY</span>
        </div>

        <section className="hero">
          <div className="hero-image">
            <span>FEATURED STORY</span>
          </div>

          <div className="hero-content">
            <p className="category">TECHNOLOGY / INNOVATION</p>
            <h2>The Future Is Being Written Today.</h2>
            <p className="description">
              Exploring the ideas, innovations and breakthroughs
              that are shaping tomorrow's world.
            </p>
            <button>EXPLORE STORIES ↗</button>
          </div>
        </section>

        <section className="latest" id="technology">
          <div className="latest-heading">
            <h2>THE LATEST</h2>
            <span>FRESH PERSPECTIVES. EVERY DAY.</span>
          </div>

          <div className="news-grid">
            <article className="news-card">
              <div className="news-image image-one"></div>
              <p>TECHNOLOGY</p>
              <h3>Artificial Intelligence Is Changing The Way We Live</h3>
              <span>THE DAILY · 5 MIN READ</span>
            </article>

            <article className="news-card">
              <div className="news-image image-two"></div>
              <p>SCIENCE</p>
              <h3>New Discoveries Are Expanding Our Understanding</h3>
              <span>THE DAILY · 4 MIN READ</span>
            </article>

            <article className="news-card">
              <div className="news-image image-three"></div>
              <p>BUSINESS</p>
              <h3>The Ideas Driving Tomorrow's Economy</h3>
              <span>THE DAILY · 6 MIN READ</span>
            </article>
          </div>
        </section>
      </main>

      <footer>
        <h2>THE DAILY<span>.</span></h2>
        <p>INDEPENDENT NEWS. INFORMED WORLD.</p>
        <small>© 2026 THE DAILY. ALL RIGHTS RESERVED.</small>
      </footer>
    </div>
  )
}

export default App
