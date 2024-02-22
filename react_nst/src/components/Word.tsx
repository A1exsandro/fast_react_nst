import React from "react"
import { WordData } from "./Words"

interface WordProps {
    word: WordData
}


const Word: React.FC<WordProps> = ({word}) => {

    return (
        <div className="border-solid border-2 border-indigo-600 w-96 rounded-xl p-3 my-2">
            {/* Opposite and Similar */}
            <div className="flex justify-between">
                <h3 className="">{word.opposite}</h3>
                <h3 className="">{word.similar}</h3>
            </div>

            {/* Main Word */}
            <h1 className="text-2xl text-center font-bold">{word.english}</h1>

            {/* Class and Flueny Level */}
            <div className="flex justify-between">
                <h3 className="">{word.class}</h3>
                <h3 className="bg-green-500 px-3 rounded-xl text-white font-bold">{word.fluency_level}</h3>
            </div>

            {/* Handle */}
            <div className="flex justify-center">
                <div className="text-red-500 mr-3 font-bold">Delete</div>
                <div className="text-blue-900 font-bold">Edit</div>
            </div>
        </div>   
    )
}

export default Word
