import React, { useState } from 'react';
import { Link } from 'react-router-dom'
import './form.css';
import axios from 'axios';
import "animate.css"

const Form = () => {


        const [showGenerated, setGenerated] = useState(false);
        const [currentIndex, setCurrentIndex] = useState(0);
        const [tripsToDisplay, setTripsToDisplay] = useState([]);
        const [result, setResult] = useState(null);
        const [values, setValues] = useState({
            StartDate: "",
            Holidays: "",
            Budget: "",
            Destinations: ""
        });


    const toggleLeftBox = () => {
        setGenerated(prevState => !prevState);
    }

    const handleChange = (e) => {
        const { name, value} = e.target;

            setValues({ ...values, [name]: value });

    }


    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log(values);

        try {
            const response = await axios.get('http://127.0.0.1:5000/api/run-script', {
                params: { 
                    date: values.StartDate, 
                    length: values.Holidays, 
                    budget: values.Budget, 
                    cities: values.Destinations 
                }
            });
            setResult(response.data)
            setTripsToDisplay(response.data.slice(0, 3));
            setGenerated(true);
            setCurrentIndex(3);
            console.log("Result:", response.data);
            console.log(tripsToDisplay)
        } catch (error) {
            console.error("Error running the Python script:", error);
        }

    };

    const handleGenerateMore = () => {
        console.log(tripsToDisplay)
        console.log(currentIndex)
        const nextIndex = currentIndex + 3;
        setTripsToDisplay([
            ...result.slice(currentIndex, currentIndex + 3)
        ]);
        
        setCurrentIndex(nextIndex);
    };

    

return (
    <div className='formBackground animate__fadeIn animate__animated fade'>
        <Link to="/" className='link'>
                <p className='logo'>WL</p>
        </Link> 
        <div className='container'>
            <div className='container-left'>
                {showGenerated &&  tripsToDisplay.length > 0 && (
                    <div className={`box2 ${showGenerated ? 'show' : ''}`}> 
                        <p className='formTitle2'>Heres what we found:</p>
                        <div className="trips">
                            {tripsToDisplay.map((trip, index) => (
                                <div key={index} className="trip">
                                    <p><strong>Price:</strong> ${trip.PRICE}</p>
                                    <p><strong>Destinations:</strong> {Array.isArray(trip.VISITS) ? trip.VISITS.join(", ") : 'N/A'}</p>
                                    <p><strong>Flights on Days:</strong> {Array.isArray(trip.DAYS) ? trip.DAYS.join(", ") : 'N/A'}</p>
                                </div>
                            ))}
                        </div>
                            {currentIndex < result.length && (
                                <button className="generate-more-btn" onClick={handleGenerateMore}>
                                    Generate More
                                </button>
                            )}
                    </div>
                )}
            </div>
            <div className='container-right'>
                <h1 className='formTitle'>Lets plan your vacation</h1>
                <div className='box'>
                <form className='form c' onSubmit={handleSubmit}>
                    <label className="edit-label" htmlFor="StartDate" draggable="false">When will you start?</label>
                    <input className="edit-input2" type="text"  name="StartDate"
                        onChange={(e) => handleChange(e)}/>
                    <div className="double-input-row">
                        <label className="edit-label" htmlFor="Holidays" draggable="false">For How Long?</label>
                        <label className="edit-label" htmlFor="Budget" draggable="false">For How Much?</label>

                        <input className="edit-input" type="text"  name="Holidays"
                        onChange={(e) => handleChange(e)}/>
                        <input className="edit-input" type="text"  name="Budget"
                        onChange={(e) => handleChange(e)}/>
                    </div>

                    <label className="edit-label" htmlFor="Destinations" draggable="false">Where To?</label>
                    <textarea className="edit-resize" name="Destinations" id="Destinations" cols="30" rows="" value={values.aboutMe}
                    onChange={(e) => handleChange(e)}></textarea>
                    
                    <button type='submit' className='edit-submit' draggable="false">Generate</button>
                </form>
                </div>
            </div>
        </div>
    </div>
    );
};

export default Form;
