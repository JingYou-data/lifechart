import anthropic
import json
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

client = anthropic.Anthropic()

def get_bazi_reading(birth_date: str, birth_time: str = None, lang: str = "zh") -> str:

    if lang == "zh":
        prompt = f"""你是一位精通八字命理的大师。请完全用中文回答，只返回JSON格式，不要有任何其他文字。

用户出生日期：{birth_date}
用户出生时间：{birth_time if birth_time else "未知"}

只返回这个JSON格式，不要加任何解释：
{{
    "title": "八字命理分析",
    "pillars": {{
        "title": "四柱八字",
        "year": "年柱内容",
        "month": "月柱内容",
        "day": "日柱内容",
        "hour": "时柱内容"
    }},
    "elements": {{
        "title": "五行分析",
        "content": "五行分析内容"
    }},
    "personality": {{
        "title": "性格特点",
        "content": "性格分析内容"
    }},
    "fortune": {{
        "title": "2026年运势",
        "content": "运势内容"
    }}
}}"""
    else:
        prompt = f"""You are a master of BaZi Chinese astrology. Respond ONLY in JSON format, no other text.

Date of birth: {birth_date}
Time of birth: {birth_time if birth_time else "unknown"}

Return ONLY this JSON, no explanation:
{{
    "title": "BaZi Destiny Analysis",
    "pillars": {{
        "title": "Four Pillars",
        "year": "Year pillar content",
        "month": "Month pillar content",
        "day": "Day pillar content",
        "hour": "Hour pillar content"
    }},
    "elements": {{
        "title": "Five Elements",
        "content": "Five elements analysis"
    }},
    "personality": {{
        "title": "Personality",
        "content": "Personality analysis"
    }},
    "fortune": {{
        "title": "2026 Fortune",
        "content": "Fortune reading"
    }}
}}"""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return message.content[0].text


app = FastAPI()

class BirthInfo(BaseModel):
    birth_date: str
    birth_time: str = None
    lang: str = "zh"

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/reading")
def get_reading(info: BirthInfo):
    result = get_bazi_reading(info.birth_date, info.birth_time, info.lang)
    # 去掉markdown代码块
    result = result.strip()
    if result.startswith("```json"):
        result = result[7:]
    if result.startswith("```"):
        result = result[3:]
    if result.endswith("```"):
        result = result[:-3]
    result = result.strip()
    try:
        parsed = json.loads(result)
        return parsed
    except:
        return {"error": result}