import './Home.css';
import { Link } from 'react-router-dom';
import "animate.css"

const Home = () => {
    return (
        <div className="homeBackground animate__fadeIn animate__animated fade">
                    <Link to="/" className='link'>
                        <p className='logo'>WL</p>
                    </Link> 
            <Link to="/form" className='link'>
                <div className="learnMore hoverEnlarge">
                    <p className='learnMoreText'>Get Started</p>
                </div>
            </Link>
        </div>
    )
}

export default Home