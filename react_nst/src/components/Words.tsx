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
        }
    ])

    return (
        <div className="">
            {
                words.map((word, i) => (
                    <Word 
                        key={i}
                        word={word}
                    />
                ))
            }
        </div>
    )
}

export default Words
