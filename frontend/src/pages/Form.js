import React, { useState } from 'react';
import { Link } from 'react-router-dom'
import './form.css';
import "animate.css"

const Form = () => {
    const [showGenerated, setGenerated] = useState(false);

    const toggleLeftBox = () => {
        setGenerated(prevState => !prevState);
    }

    const [values, setValues] = useState({
        StartDate: "",
        Holidays: "",
        Budget: "",
        Destinations: []
    })

    const handleChange = (e) => {
        const { name, value} = e.target;

            setValues({ ...values, [name]: value });
    }

    const handleSubmit = async (e) => {
        e.preventDefault()
        console.log(values)

        // const response = await fetch('http://localhost:4000/api/users/' + user.Email, {
        //     method: 'PATCH',
        //     body: JSON.stringify(User),
        //     headers: {
        //         'Content-Type': 'application/json'
        //     }
        // })

        // const json = await response.json()
        
        // if (response.ok){
        //     setFormSubmitted(true)
        //     setTimeout(() => {
        //        setFormSubmitted(false)
        //     }, 3000)

        //     //dispatch({type: 'SET_USER', payload: json})

        //     console.log("new data added, json")
        //     console.log(json)
        // }
        toggleLeftBox()

    }

return (
    <div className='formBackground animate__fadeIn animate__animated fade'>
        <Link to="/" className='link'>
                <p className='logo'>WL</p>
        </Link> 
        <div className='container'>
            <div className='container-left'>
                {showGenerated && (
                    <div className={`box2 ${showGenerated ? 'show' : ''}`}> 
                        <p className='formTitle2'>Heres what we found:</p>
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
                    <textarea className="edit-resize" name="Destinations" id="aboutMe" cols="30" rows="" value={values.aboutMe}
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
