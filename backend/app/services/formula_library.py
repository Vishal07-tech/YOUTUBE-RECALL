"""Standard formula library used when a video is an all-in-one formula sheet.

Many short "formula sheet" videos have no captions, so the only available source
text is the title/description. This library makes sure every standard formula for
the topics the creator lists is still shown instead of an arbitrary few.
"""

import re
from typing import Any, Dict, List, Tuple

FORMULA_SHEET_PATTERN = (
    r"formula\s*sheet|all[- ]?in[- ]?one.{0,40}formula|all\s+(?:math(?:ematics|s)?\s+)?formulas|"
    r"important\s+formulas|maths\s+tricks|formula\s+chart|formulas\s+in\s+one\s+video"
)

TOPIC_PATTERNS: Dict[str, str] = {
    "numbers": r"\b(numbers?|number system|hcf|lcm|percentage|profit|loss|discount|interest|ratio|proportion)\b",
    "indices": r"\b(indices|exponents?|powers?|surds?|roots?)\b",
    "algebra": r"\b(algebra|polynomial|quadratic|linear equation|factorisation|factorization)\b",
    "identities": r"\b(identit(?:y|ies))\b",
    "geometry": r"\b(geometry|triangle|circle|square|rectangle|area|perimeter|surface area|volume|pythagoras|heron|quadrilateral|rhombus|trapezium|cylinder|cone|sphere|cuboid|cube)\b",
    "trigonometry": r"\b(trigonometry|trigonometric|sin\b|cos\b|tan\b|angle|heights?|distances?)\b",
    "statistics": r"\b(statistics|mean|median|mode|probability|average)\b",
}

# Each entry: (name, LaTeX formula, variables glossary, plain-English use)
FORMULA_LIBRARY: Dict[str, List[Tuple[str, str, str, str]]] = {
    "numbers": [
        ("HCF-LCM Product Rule", r"$$a \times b = \mathrm{HCF}(a,b) \times \mathrm{LCM}(a,b)$$", "a, b: positive integers.", "Links the product of two numbers to their HCF and LCM."),
        ("Percentage", r"$$\mathrm{Percentage} = \frac{\mathrm{Part}}{\mathrm{Whole}} \times 100$$", "Part: subset value; Whole: total value.", "Converts a part-to-whole ratio into a percentage."),
        ("Profit Percent", r"$$\mathrm{Profit}\% = \frac{\mathrm{SP} - \mathrm{CP}}{\mathrm{CP}} \times 100$$", "SP: selling price; CP: cost price.", "Measures profit relative to cost price."),
        ("Loss Percent", r"$$\mathrm{Loss}\% = \frac{\mathrm{CP} - \mathrm{SP}}{\mathrm{CP}} \times 100$$", "SP: selling price; CP: cost price.", "Measures loss relative to cost price."),
        ("Selling Price from Profit", r"$$\mathrm{SP} = \mathrm{CP}\left(1 + \frac{p}{100}\right)$$", "p: profit percent.", "Finds selling price directly from cost and profit percent."),
        ("Discount Percent", r"$$\mathrm{Discount}\% = \frac{\mathrm{MP} - \mathrm{SP}}{\mathrm{MP}} \times 100$$", "MP: marked price; SP: selling price.", "Measures discount relative to marked price."),
        ("Simple Interest", r"$$\mathrm{SI} = \frac{P \times R \times T}{100}$$", "P: principal; R: rate percent per year; T: time in years.", "Calculates simple interest."),
        ("Amount from Simple Interest", r"$$A = P + \mathrm{SI}$$", "A: final amount; P: principal; SI: simple interest.", "Adds interest back to the principal."),
        ("Ratio and Proportion", r"$$\frac{a}{b} = \frac{c}{d} \implies ad = bc$$", "a:b and c:d are equal ratios.", "Cross-multiplication rule for proportions."),
    ],
    "indices": [
        ("Product of Powers", r"$$a^m \times a^n = a^{m+n}$$", "a: base; m, n: exponents.", "Multiply powers with the same base by adding exponents."),
        ("Quotient of Powers", r"$$\frac{a^m}{a^n} = a^{m-n}$$", "a: non-zero base.", "Divide powers with the same base by subtracting exponents."),
        ("Power of a Power", r"$$(a^m)^n = a^{mn}$$", "a: base; m, n: exponents.", "Nested powers multiply their exponents."),
        ("Zero Exponent", r"$$a^0 = 1 \quad (a \neq 0)$$", "a: non-zero base.", "Any non-zero base raised to zero equals one."),
        ("Negative Exponent", r"$$a^{-n} = \frac{1}{a^n}$$", "a: non-zero base; n: positive integer.", "A negative exponent means reciprocal."),
        ("Power of a Product", r"$$(ab)^n = a^n b^n$$", "a, b: bases; n: exponent.", "Distributes an exponent over multiplication."),
        ("Power of a Quotient", r"$$\left(\frac{a}{b}\right)^n = \frac{a^n}{b^n}$$", "b: non-zero denominator.", "Distributes an exponent over division."),
        ("Fractional Exponent", r"$$a^{m/n} = \sqrt[n]{a^m}$$", "n: root index; m: power.", "Converts a rational exponent into a radical."),
    ],
    "algebra": [
        ("Square of a Sum", r"$$(a+b)^2 = a^2 + 2ab + b^2$$", "a, b: real numbers.", "Expands a squared binomial."),
        ("Square of a Difference", r"$$(a-b)^2 = a^2 - 2ab + b^2$$", "a, b: real numbers.", "Expands a squared difference."),
        ("Difference of Squares", r"$$(a+b)(a-b) = a^2 - b^2$$", "a, b: real numbers.", "Factors a difference of two squares."),
        ("Square of a Trinomial", r"$$(a+b+c)^2 = a^2+b^2+c^2+2ab+2bc+2ca$$", "a, b, c: real numbers.", "Expands the square of a three-term sum."),
        ("Cube of a Sum", r"$$(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$$", "a, b: real numbers.", "Expands a cubed binomial."),
        ("Cube of a Difference", r"$$(a-b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$$", "a, b: real numbers.", "Expands a cubed difference."),
        ("Sum of Cubes", r"$$a^3 + b^3 = (a+b)(a^2 - ab + b^2)$$", "a, b: real numbers.", "Factors a sum of cubes."),
        ("Difference of Cubes", r"$$a^3 - b^3 = (a-b)(a^2 + ab + b^2)$$", "a, b: real numbers.", "Factors a difference of cubes."),
        ("Three-Variable Cube Identity", r"$$a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$$", "a, b, c: real numbers.", "Key factorization identity for three variables."),
        ("Three-Variable Zero-Sum Case", r"$$a+b+c=0 \implies a^3+b^3+c^3 = 3abc$$", "a, b, c: real numbers.", "Special case of the cube identity when the sum is zero."),
        ("Quadratic Formula", r"$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$", "a, b, c: coefficients of ax^2+bx+c=0.", "Solves any quadratic equation."),
        ("Quadratic Discriminant", r"$$D = b^2 - 4ac$$", "a, b, c: coefficients.", "Determines the nature of quadratic roots."),
        ("Remainder Theorem", r"$$p(x) \div (x-a) \text{ leaves remainder } p(a)$$", "p(x): polynomial; a: constant.", "Evaluates a polynomial at a to find the remainder."),
        ("Factor Theorem", r"$$p(a)=0 \iff (x-a) \text{ is a factor of } p(x)$$", "p(x): polynomial.", "Connects roots and factors of polynomials."),
        ("Linear Pair Product", r"$$(x+a)(x+b) = x^2 + (a+b)x + ab$$", "x: variable; a, b: constants.", "Quick expansion for two linear factors."),
    ],
    "identities": [
        ("Square of a Sum", r"$$(a+b)^2 = a^2 + 2ab + b^2$$", "a, b: real numbers.", "Fundamental algebraic identity."),
        ("Square of a Difference", r"$$(a-b)^2 = a^2 - 2ab + b^2$$", "a, b: real numbers.", "Fundamental algebraic identity."),
        ("Difference of Squares", r"$$a^2 - b^2 = (a-b)(a+b)$$", "a, b: real numbers.", "Difference of squares factorization."),
        ("Square of a Trinomial", r"$$(a+b+c)^2 = a^2+b^2+c^2+2(ab+bc+ca)$$", "a, b, c: real numbers.", "Three-term square identity."),
        ("Cube of a Sum", r"$$(a+b)^3 = a^3+b^3+3ab(a+b)$$", "a, b: real numbers.", "Compact cube-of-sum identity."),
        ("Cube of a Difference", r"$$(a-b)^3 = a^3-b^3-3ab(a-b)$$", "a, b: real numbers.", "Compact cube-of-difference identity."),
        ("Sum of Cubes", r"$$a^3+b^3 = (a+b)(a^2-ab+b^2)$$", "a, b: real numbers.", "Sum-of-cubes factorization."),
        ("Difference of Cubes", r"$$a^3-b^3 = (a-b)(a^2+ab+b^2)$$", "a, b: real numbers.", "Difference-of-cubes factorization."),
        ("Three-Variable Cube Identity", r"$$a^3+b^3+c^3-3abc = (a+b+c)(a^2+b^2+c^2-ab-bc-ca)$$", "a, b, c: real numbers.", "High-yield competitive exam identity."),
    ],
    "geometry": [
        ("Pythagoras Theorem", r"$$a^2 + b^2 = c^2$$", "a, b: legs; c: hypotenuse of a right triangle.", "Relates the sides of a right-angled triangle."),
        ("Area of a Triangle", r"$$A = \frac{1}{2}bh$$", "b: base; h: height.", "Basic triangle area formula."),
        ("Heron's Formula", r"$$s = \frac{a+b+c}{2}, \quad A = \sqrt{s(s-a)(s-b)(s-c)}$$", "a, b, c: side lengths; s: semi-perimeter.", "Finds triangle area from three sides."),
        ("Area of a Rectangle", r"$$A = l \times b$$", "l: length; b: breadth.", "Rectangle area."),
        ("Perimeter of a Rectangle", r"$$P = 2(l+b)$$", "l: length; b: breadth.", "Rectangle perimeter."),
        ("Area of a Square", r"$$A = a^2$$", "a: side length.", "Square area."),
        ("Area of a Circle", r"$$A = \pi r^2$$", "r: radius.", "Circle area."),
        ("Circumference of a Circle", r"$$C = 2\pi r = \pi d$$", "r: radius; d: diameter.", "Circle perimeter."),
        ("Area of a Parallelogram", r"$$A = b \times h$$", "b: base; h: perpendicular height.", "Parallelogram area."),
        ("Area of a Rhombus", r"$$A = \frac{1}{2}d_1 d_2$$", "d1, d2: diagonals.", "Rhombus area from diagonals."),
        ("Area of a Trapezium", r"$$A = \frac{1}{2}(a+b)h$$", "a, b: parallel sides; h: height.", "Trapezium area."),
        ("Surface Area of a Cube", r"$$\mathrm{TSA} = 6a^2$$", "a: edge length.", "Total surface area of a cube."),
        ("Volume of a Cube", r"$$V = a^3$$", "a: edge length.", "Cube volume."),
        ("Surface Area of a Cuboid", r"$$\mathrm{TSA} = 2(lb + bh + hl)$$", "l, b, h: length, breadth, height.", "Total surface area of a cuboid."),
        ("Volume of a Cuboid", r"$$V = l \times b \times h$$", "l, b, h: dimensions.", "Cuboid volume."),
        ("Curved Surface Area of a Cylinder", r"$$\mathrm{CSA} = 2\pi rh$$", "r: radius; h: height.", "Lateral surface area of a cylinder."),
        ("Total Surface Area of a Cylinder", r"$$\mathrm{TSA} = 2\pi r(r+h)$$", "r: radius; h: height.", "Total surface area of a cylinder."),
        ("Volume of a Cylinder", r"$$V = \pi r^2 h$$", "r: radius; h: height.", "Cylinder volume."),
        ("Curved Surface Area of a Cone", r"$$\mathrm{CSA} = \pi r l$$", "r: radius; l: slant height.", "Lateral surface area of a cone."),
        ("Total Surface Area of a Cone", r"$$\mathrm{TSA} = \pi r(r+l)$$", "r: radius; l: slant height.", "Total surface area of a cone."),
        ("Volume of a Cone", r"$$V = \frac{1}{3}\pi r^2 h$$", "r: radius; h: height.", "Cone volume."),
        ("Surface Area of a Sphere", r"$$A = 4\pi r^2$$", "r: radius.", "Sphere surface area."),
        ("Volume of a Sphere", r"$$V = \frac{4}{3}\pi r^3$$", "r: radius.", "Sphere volume."),
        ("Distance Formula", r"$$d = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}$$", "(x1,y1), (x2,y2): two points.", "Distance between two coordinate points."),
        ("Midpoint Formula", r"$$M = \left(\frac{x_1+x_2}{2}, \frac{y_1+y_2}{2}\right)$$", "endpoints (x1,y1) and (x2,y2).", "Midpoint of a line segment."),
    ],
    "trigonometry": [
        ("Basic Sine Ratio", r"$$\sin\theta = \frac{\mathrm{Perpendicular}}{\mathrm{Hypotenuse}}$$", "theta: acute angle in a right triangle.", "Defines sine."),
        ("Basic Cosine Ratio", r"$$\cos\theta = \frac{\mathrm{Base}}{\mathrm{Hypotenuse}}$$", "theta: acute angle.", "Defines cosine."),
        ("Basic Tangent Ratio", r"$$\tan\theta = \frac{\mathrm{Perpendicular}}{\mathrm{Base}}$$", "theta: acute angle.", "Defines tangent."),
        ("Tangent as Sine over Cosine", r"$$\tan\theta = \frac{\sin\theta}{\cos\theta}$$", "theta: angle.", "Relates tangent to sine and cosine."),
        ("Cotangent as Cosine over Sine", r"$$\cot\theta = \frac{\cos\theta}{\sin\theta}$$", "theta: angle.", "Reciprocal tangent identity."),
        ("Pythagorean Trigonometric Identity", r"$$\sin^2\theta + \cos^2\theta = 1$$", "theta: angle.", "Most important trigonometry identity."),
        ("Secant Identity", r"$$1 + \tan^2\theta = \sec^2\theta$$", "theta: angle.", "Derived from the Pythagorean identity."),
        ("Cosecant Identity", r"$$1 + \cot^2\theta = \csc^2\theta$$", "theta: angle.", "Derived by dividing by sin^2(theta)."),
        ("Reciprocal of Cosine", r"$$\sec\theta = \frac{1}{\cos\theta}$$", "theta: angle.", "Defines secant."),
        ("Reciprocal of Sine", r"$$\csc\theta = \frac{1}{\sin\theta}$$", "theta: angle.", "Defines cosecant."),
        ("Complementary Angle Identity", r"$$\sin(90^\circ - \theta) = \cos\theta$$", "theta: angle in degrees.", "Relates complementary angles."),
        ("Height and Distance", r"$$\tan\theta = \frac{\mathrm{Height}}{\mathrm{Distance}}$$", "theta: angle of elevation.", "Solves height-and-distance problems."),
    ],
    "statistics": [
        ("Arithmetic Mean", r"$$\bar{x} = \frac{\sum x_i}{n}$$", "x_i: observations; n: count.", "Average of a data set."),
        ("Probability", r"$$P(E) = \frac{\mathrm{Favourable\ outcomes}}{\mathrm{Total\ outcomes}}$$", "E: event.", "Classical probability of an event."),
        ("Range", r"$$\mathrm{Range} = \mathrm{Maximum} - \mathrm{Minimum}$$", "data set extremes.", "Spread of the data."),
    ],
}


def is_formula_sheet(text: str) -> bool:
    return bool(re.search(FORMULA_SHEET_PATTERN, text or "", re.IGNORECASE))


def build_formula_sheet_formulas(title: str, transcript_text: str, chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Return every standard formula for topics listed in a formula-sheet video."""
    source = f"{title or ''} {transcript_text or ''}"
    if not is_formula_sheet(source):
        return []

    def timestamp_for(pattern: str) -> str:
        for chunk in chunks or []:
            if re.search(pattern, chunk.get("content", "") or "", re.IGNORECASE):
                return chunk.get("timestamp_label", "00:00")
        return "00:00"

    seen = set()
    formulas: List[Dict[str, Any]] = []
    for topic, topic_pattern in TOPIC_PATTERNS.items():
        if not re.search(topic_pattern, source, re.IGNORECASE):
            continue
        ts_label = timestamp_for(topic_pattern)
        for name, latex, variables, explanation in FORMULA_LIBRARY.get(topic, []):
            key = re.sub(r"\s+", "", latex)
            if key in seen:
                continue
            seen.add(key)
            formulas.append({
                "name": name,
                "formula_latex": latex,
                "variables": variables,
                "explanation": explanation,
                "timestamp_label": ts_label,
            })
    return formulas
