import os
import io
import base64
from PIL import Image, ImageDraw

def main():
    src = r'd:\Workspace\projects\Readme\Confident Creative Director Portrait.png'
    dest_svg = r'd:\Workspace\projects\Readme\Sushmitadasari-main\assets\ankit-hero-portrait.svg'

    im = Image.open(src).convert('RGBA')

    # Bounding box of headshot circle in Confident Creative Director Portrait.png: center=(590, 425), radius=420
    cx, cy, r = 590, 425, 420
    crop_box = (cx - r, cy - r, cx + r, cy + r)
    cropped = im.crop(crop_box)

    # Smooth circle mask
    mask = Image.new('L', (r * 2, r * 2), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, r * 2, r * 2), fill=255)
    cropped.putalpha(mask)

    size = 512
    res = cropped.resize((size, size), Image.Resampling.LANCZOS)

    # Place on matching emerald canvas background
    bg = Image.new('RGB', (size, size), (11, 31, 23))
    bg.paste(res, (0, 0), res)

    buf = io.BytesIO()
    bg.save(buf, format='JPEG', quality=93, optimize=True)
    b64_data = base64.b64encode(buf.getvalue()).decode('ascii')

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="1200" height="480" role="img" aria-labelledby="hero-title hero-desc">
  <title id="hero-title">Ankit Kumar — Engineering intelligent systems. Shipping real products.</title>
  <desc id="hero-desc">AI Engineer, Full-Stack Developer. Building LLM systems, RAG pipelines, and production web applications.</desc>

  <defs>
    <radialGradient id="hero-bg" cx="72%" cy="38%" r="80%">
      <stop offset="0" stop-color="#0B1F17"/>
      <stop offset=".55" stop-color="#0A1612"/>
      <stop offset="1" stop-color="#060E0A"/>
    </radialGradient>
    <radialGradient id="hero-light-a" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#1A6B4A" stop-opacity=".75"/>
      <stop offset="1" stop-color="#1A6B4A" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="hero-light-b" cx="50%" cy="50%" r="50%">
      <stop offset="0" stop-color="#7BC7A4" stop-opacity=".28"/>
      <stop offset="1" stop-color="#7BC7A4" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="hero-name-grad" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="520" y2="0">
      <stop offset="0" stop-color="#F0F8F3"/>
      <stop offset=".55" stop-color="#B5E5CB"/>
      <stop offset="1" stop-color="#7BC7A4"/>
    </linearGradient>
    <linearGradient id="hero-sheen" gradientUnits="userSpaceOnUse" x1="-260" y1="0" x2="-40" y2="0">
      <stop offset="0" stop-color="#F0F8F3" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".85"/>
      <stop offset="1" stop-color="#F0F8F3" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate" values="0 0;760 0;760 0" keyTimes="0;.35;1" dur="8s" begin="3s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="hero-scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#B5E5CB" stop-opacity="0"/>
      <stop offset=".5" stop-color="#B5E5CB" stop-opacity=".07"/>
      <stop offset="1" stop-color="#B5E5CB" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-rule" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#7BC7A4" stop-opacity="0"/>
      <stop offset=".2" stop-color="#B5E5CB"/>
      <stop offset=".75" stop-color="#1A6B4A"/>
      <stop offset="1" stop-color="#1A6B4A" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="hero-orbit-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#B5E5CB" stop-opacity=".6"/>
      <stop offset="1" stop-color="#1A6B4A" stop-opacity=".05"/>
    </linearGradient>
    <linearGradient id="hero-photo-ring" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#B5E5CB"/>
      <stop offset=".4" stop-color="#1A6B4A"/>
      <stop offset="1" stop-color="#7BC7A4"/>
    </linearGradient>
    <linearGradient id="hero-photo-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset=".5" stop-color="#FFFFFF" stop-opacity=".18"/>
      <stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <radialGradient id="hero-photo-wash" cx="50%" cy="30%" r="80%">
      <stop offset="0" stop-color="#0C241B"/>
      <stop offset=".6" stop-color="#0A1612"/>
      <stop offset="1" stop-color="#060E0A"/>
    </radialGradient>
    <clipPath id="hero-photo-circle">
      <circle cx="965" cy="232" r="126"/>
    </clipPath>
    <pattern id="hero-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="#7BC7A4" stroke-opacity=".07" stroke-width="1"/>
    </pattern>
    <radialGradient id="hero-grid-fade" cx="68%" cy="45%" r="55%">
      <stop offset="0" stop-color="#fff"/>
      <stop offset="1" stop-color="#000"/>
    </radialGradient>
    <mask id="hero-grid-mask">
      <rect width="1200" height="480" fill="url(#hero-grid-fade)"/>
    </mask>
    <filter id="hero-glow" x="-20%" y="-200%" width="140%" height="500%">
      <feGaussianBlur stdDeviation="4" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <clipPath id="hero-clip"><rect width="1200" height="480" rx="20"/></clipPath>
  </defs>

  <style>
    .hero-serif {{ font-family: Georgia, "Iowan Old Style", "Palatino Linotype", "Times New Roman", serif; }}
    .hero-mono {{ font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace; }}
    .hero-sans {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; }}

    .hero-rise {{ animation: hero-rise 1.4s cubic-bezier(.16,1,.3,1) both; }}
    .hero-fade {{ animation: hero-fade 1.6s cubic-bezier(.16,1,.3,1) both; }}
    .d1 {{ animation-delay: .15s; }} .d2 {{ animation-delay: .35s; }} .d3 {{ animation-delay: .6s; }}
    .d4 {{ animation-delay: .9s; }} .d5 {{ animation-delay: 1.2s; }} .d6 {{ animation-delay: 1.5s; }}

    .hero-portrait {{ animation: hero-photo 1.5s cubic-bezier(.16,1,.3,1) .4s both; }}
    .hero-draw {{ stroke-dasharray: 900; stroke-dashoffset: 900; animation: hero-draw 2.4s cubic-bezier(.65,0,.35,1) .9s forwards; }}
    .hero-signal {{ stroke-dasharray: 500; stroke-dashoffset: 500; animation: hero-draw 2.2s cubic-bezier(.65,0,.35,1) 2.2s forwards; }}
    @keyframes hero-photo {{ from {{ opacity: 0; transform: scale(.92); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-rise {{ from {{ opacity: 0; transform: translateY(18px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes hero-fade {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes hero-draw {{ to {{ stroke-dashoffset: 0; }} }}

    @media (prefers-reduced-motion: reduce) {{
      .hero-rise, .hero-fade, .hero-portrait {{ animation: none; }}
      .hero-draw, .hero-signal {{ animation: none; stroke-dashoffset: 0; }}
    }}
  </style>

  <g clip-path="url(#hero-clip)">
    <!-- Canvas -->
    <rect width="1200" height="480" fill="url(#hero-bg)"/>

    <!-- Slow light fields -->
    <ellipse cx="900" cy="140" rx="420" ry="300" fill="url(#hero-light-a)">
      <animateTransform attributeName="transform" type="translate" values="0 0; -60 30; 0 0" dur="22s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>
    <ellipse cx="180" cy="460" rx="360" ry="220" fill="url(#hero-light-b)">
      <animateTransform attributeName="transform" type="translate" values="0 0; 70 -25; 0 0" dur="28s" repeatCount="indefinite" calcMode="spline" keySplines=".45 0 .55 1; .45 0 .55 1"/>
    </ellipse>

    <!-- Technical grid -->
    <rect width="1200" height="480" fill="url(#hero-grid)" mask="url(#hero-grid-mask)"/>

    <!-- Slow scan line -->
    <rect x="0" y="-140" width="1200" height="140" fill="url(#hero-scan)">
      <animate attributeName="y" values="-140;480" dur="11s" begin="2s" repeatCount="indefinite"/>
    </rect>

    <!-- Drifting particles -->
    <g fill="#B5E5CB">
      <circle cx="560" cy="120" r="1.4"><animate attributeName="opacity" values="0;.9;0" dur="4.2s" repeatCount="indefinite"/><animate attributeName="cy" values="120;96" dur="4.2s" repeatCount="indefinite"/></circle>
      <circle cx="700" cy="70" r="1.1"><animate attributeName="opacity" values="0;.8;0" dur="5.6s" begin="1s" repeatCount="indefinite"/><animate attributeName="cy" values="70;48" dur="5.6s" begin="1s" repeatCount="indefinite"/></circle>
      <circle cx="1120" cy="380" r="1.6"><animate attributeName="opacity" values="0;.9;0" dur="4.8s" begin="2s" repeatCount="indefinite"/><animate attributeName="cy" values="380;352" dur="4.8s" begin="2s" repeatCount="indefinite"/></circle>
      <circle cx="760" cy="420" r="1.2"><animate attributeName="opacity" values="0;.7;0" dur="6s" begin=".5s" repeatCount="indefinite"/><animate attributeName="cy" values="420;396" dur="6s" begin=".5s" repeatCount="indefinite"/></circle>
      <circle cx="1060" cy="60" r="1.3"><animate attributeName="opacity" values="0;.85;0" dur="5s" begin="3s" repeatCount="indefinite"/><animate attributeName="cy" values="60;40" dur="5s" begin="3s" repeatCount="indefinite"/></circle>
      <circle cx="640" cy="250" r="1"><animate attributeName="opacity" values="0;.7;0" dur="4.4s" begin="2.5s" repeatCount="indefinite"/><animate attributeName="cy" values="250;226" dur="4.4s" begin="2.5s" repeatCount="indefinite"/></circle>
      <circle cx="320" cy="180" r="1.5"><animate attributeName="opacity" values="0;.8;0" dur="5.2s" begin="1.8s" repeatCount="indefinite"/><animate attributeName="cy" values="180;155" dur="5.2s" begin="1.8s" repeatCount="indefinite"/></circle>
    </g>

    <!-- Terminal command pill at top left -->
    <g class="hero-fade d1" transform="translate(64 56)">
      <rect width="310" height="32" rx="16" fill="#0A1612" stroke="#7BC7A4" stroke-opacity=".3"/>
      <circle cx="18" cy="16" r="4" fill="#7BC7A4">
        <animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/>
      </circle>
      <text class="hero-mono" x="32" y="20" font-size="11.5" fill="#8FA99A">~/ankit<tspan fill="#7BC7A4"> $ </tspan><tspan fill="#F0F8F3">build --intelligent</tspan></text>
      <rect x="285" y="10" width="7" height="12" fill="#B5E5CB">
        <animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1.1s" repeatCount="indefinite"/>
      </rect>
    </g>

    <!-- Orbital rings around portrait -->
    <g transform="translate(965 232)" class="hero-fade d3">
      <circle r="212" fill="none" stroke="#7BC7A4" stroke-opacity=".1" stroke-dasharray="1 10">
        <animateTransform attributeName="transform" type="rotate" from="0" to="-360" dur="140s" repeatCount="indefinite"/>
      </circle>
      <circle r="190" fill="none" stroke="url(#hero-orbit-grad)" stroke-width="1"/>
      <circle r="165" fill="none" stroke="#7BC7A4" stroke-opacity=".16" stroke-dasharray="2 7"/>
      <g>
        <animateTransform attributeName="transform" type="rotate" from="360" to="0" dur="95s" repeatCount="indefinite"/>
        <circle cx="0" cy="165" r="2.5" fill="#F0F8F3"/>
        <circle cx="-165" cy="0" r="2" fill="#7BC7A4" fill-opacity=".7"/>
      </g>
    </g>

    <!-- Right Circle: Portrait & Photo -->
    <g class="hero-portrait">
      <!-- Outer subtle tech tick ring -->
      <circle cx="965" cy="232" r="140" fill="none" stroke="#7BC7A4" stroke-opacity=".25" stroke-dasharray="6 18">
        <animateTransform attributeName="transform" type="rotate" from="0 965 232" to="360 965 232" dur="50s" repeatCount="indefinite"/>
      </circle>
      <circle cx="965" cy="232" r="133" fill="none" stroke="#1A6B4A" stroke-opacity=".4" stroke-width="1"/>

      <!-- Background circle behind photo -->
      <circle cx="965" cy="232" r="126" fill="url(#hero-photo-wash)"/>

      <!-- Photo with circular clip path -->
      <g clip-path="url(#hero-photo-circle)">
        <image href="data:image/jpeg;base64,{b64_data}" x="839" y="106" width="252" height="252" preserveAspectRatio="xMidYMid slice"/>
        <!-- Diagonal glass sheen animation across portrait -->
        <rect x="800" y="80" width="80" height="300" fill="url(#hero-photo-sheen)" transform="skewX(-18)">
          <animate attributeName="x" values="700;1200;1200" keyTimes="0;.35;1" dur="10s" begin="3s" repeatCount="indefinite"/>
        </rect>
      </g>

      <!-- Emerald neon ring border -->
      <circle cx="965" cy="232" r="126" fill="none" stroke="url(#hero-photo-ring)" stroke-width="2.2"/>

      <!-- Reticle / crosshair tech marks -->
      <path d="M835 232 h-10 M1095 232 h10 M965 102 v-10 M965 362 v10" stroke="#7BC7A4" stroke-opacity=".5" stroke-width="1.5"/>
    </g>

    <!-- Floating orbital node tags -->
    <g transform="translate(965 232)" class="hero-fade d4">
      <g class="hero-mono" font-size="10" letter-spacing="1.6" fill="#8FA99A">
        <g transform="translate(-115 -148)"><circle r="3" fill="#7BC7A4"/><text x="10" y="3.5">AI / LLM</text></g>
        <g transform="translate(130 -105)"><circle r="3" fill="#7BC7A4"/><text x="10" y="3.5">RAG</text></g>
        <g transform="translate(130 115)"><circle r="3" fill="#7BC7A4"/><text x="10" y="3.5">FASTAPI</text></g>
        <g transform="translate(-145 55)"><circle r="3" fill="#7BC7A4"/><text x="-10" y="3.5" text-anchor="end">NEXT.JS</text></g>
      </g>
    </g>

    <!-- Signal path connecting text to portrait -->
    <path class="hero-signal" d="M620 338 C 700 334, 760 326, 800 300 S 830 260, 839 250" fill="none" stroke="#7BC7A4" stroke-opacity=".4" stroke-width="1.2"/>
    <circle cx="620" cy="338" r="3" fill="#F0F8F3" filter="url(#hero-glow)" opacity=".9">
      <animateMotion dur="5s" repeatCount="indefinite" begin="4s" path="M620 338 C 700 334, 760 326, 800 300 S 830 260, 839 250" keyPoints="0;1" keyTimes="0;1" calcMode="spline" keySplines=".45 0 .55 1"/>
    </circle>

    <!-- Name and title text -->
    <g class="hero-rise d1">
      <text class="hero-mono" x="64" y="128" font-size="13" letter-spacing="3" fill="#7BC7A4">AI ENGINEER  ·  FULL-STACK DEVELOPER</text>
    </g>
    <g class="hero-rise d2">
      <text class="hero-serif" x="60" y="206" font-size="70" font-weight="300" letter-spacing="-2" fill="url(#hero-name-grad)">Ankit Kumar</text>
    </g>
    <g class="hero-rise d3">
      <text class="hero-serif" x="62" y="206" font-size="70" font-weight="300" letter-spacing="-2" fill="url(#hero-sheen)">Ankit Kumar</text>
    </g>

    <!-- Horizontal rule -->
    <path class="hero-draw" d="M62 232 H680" stroke="url(#hero-rule)" stroke-width="1"/>

    <g class="hero-rise d4">
      <text class="hero-sans" x="64" y="272" font-size="19" fill="#ACB6B0">Building LLM systems, RAG pipelines, and production web apps.</text>
    </g>

    <!-- Stats chips -->
    <g class="hero-rise d5">
      <text class="hero-mono" x="64" y="320" font-size="12" letter-spacing="2" fill="#7BC7A4">SHIPPED</text>
      <text class="hero-sans" x="142" y="320" font-size="13.5" fill="#C8D5CC">20+ client projects  ·  5 medical business platforms  ·  RAG chatbots</text>
    </g>
    <g class="hero-rise d6">
      <text class="hero-mono" x="64" y="354" font-size="12" letter-spacing="2" fill="#7BC7A4">STACK</text>
      <text class="hero-sans" x="128" y="354" font-size="13.5" fill="#C8D5CC">Next.js  ·  FastAPI  ·  TypeScript  ·  Python  ·  PostgreSQL  ·  Docker</text>
    </g>

    <!-- Location -->
    <g class="hero-fade d6">
      <text class="hero-mono" x="64" y="424" font-size="11" letter-spacing="2.5" fill="#5A7A68">BANGALORE, IN  ·  FREELANCE  ·  OPEN TO OPPORTUNITIES</text>
    </g>
  </g>
</svg>'''

    with open(dest_svg, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    print(f'Done! Successfully updated {dest_svg}')

if __name__ == '__main__':
    main()
