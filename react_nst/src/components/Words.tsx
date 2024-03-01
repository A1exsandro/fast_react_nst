import { useState } from "react"
import Word from "./Word"

export interface WordData {
    english: string;
    opposite: string;
    similar: string;
    class: string;
    fluency_level: string;
}

const Words = () => {
    const [words, setWords] = useState<WordData[]>([
        {
            english: 'Fast',
            opposite: 'Slow',
            similar: 'Fat',
            class: 'Adjective',
            fluency_level: 'beginner',
        },
        {
            english: 'Cold',
            opposite: 'Hot',
            similar: 'Could',
            class: '',
            fluency_level: 'beginner',
        },
        {
            english: 'Big',
            opposite: 'Small',
            similar: '',
            class: 'Adjective',
            fluency_level: 'beginner',
        },
    ])

    return (
        <div className="flex flex-col">
            <div className="bg-blue-500 w-screen p-2 mb-2">
                <h1 className="text-white font-bold">Words</h1>
            </div>
            <div className="flex flex-col items-center">
                {
                    words.map((word, i) => (
                        <Word 
                            key={i}
                            word={word}
                        />
                    ))
                }
            </div>
        </div>
    )
}

export default Words
