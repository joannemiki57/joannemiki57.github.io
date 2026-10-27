#!/usr/bin/env python3
"""Generate the static site from the content below.

Run from anywhere:  python3 _build/build.py
Edit the CONTENT section, re-run, and commit the generated .html files.
"""
import html
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =====================================================================
# CONTENT
# =====================================================================

SITE = {
    "first": "Joanne",
    "last": "Yun",
    "full": "Junghyun (Joanne) Yun",
    "email": "jyun45@wisc.edu",
    "scholar": "https://scholar.google.com/citations?user=6ZmnC-cAAAAJ&hl=en",
    "github": "https://github.com/joannemiki57",
    "linkedin": "https://www.linkedin.com/in/joannejyun/",
    "cv_pdf": "assets/pdf/Joanne_Yun_CV.pdf",
    "updated": "October 26, 2026",
}

ABOUT_HTML = """
<p>I'm a master's student in <a href="https://www.engr.wisc.edu/department/industrial-systems-engineering/">Industrial &amp; Systems Engineering</a> at the <a href="https://www.wisc.edu/">University of Wisconsin–Madison</a>, where I'm a research assistant in the <a href="https://feap.wiscweb.wisc.edu/">Flexible Electronics &amp; Additive Printing (FEAP) Lab</a> advised by <a href="https://directory.engr.wisc.edu/ie/faculty/qin_hantang">Prof. Hantang Qin</a>. This past summer I was a research intern in Prof. Martin Jun's Laboratory for Advanced Multiscale Manufacturing (LAMM) at Purdue University.</p>

<p>I did my B.S. in Industrial Engineering at <a href="https://www.ajou.ac.kr/en/index.do">Ajou University</a> in Suwon, South Korea, where I finished first in my class of 139, and spent my final undergraduate year at UW–Madison as a visiting student. At Ajou I worked in Prof. Jooyeon Lee's New Industrial Convergence R&amp;D Lab on solar-panel telemetry and a microfluidic sweat sensor.</p>

<p>My research is machine learning for manufacturing. Right now I'm most interested in <b>sound</b>: whether a microphone next to a machine can tell us what the process is actually doing, layer by layer. I also work on visual defect inspection and on models that still hold up when the data comes from different machines and labs.</p>

<p>I like to learn new stuff, and my projects show it: inkjet printing, laser powder bed fusion audio, camera calibration, an oral cancer screening app. Manufacturing is where most of them meet. Outside the lab I play violin, build Lego, and keep a long list of movies and books to get through.</p>

<p>Feel free to <a href="mailto:jyun45@wisc.edu">reach out</a> if you'd like to chat about any of this! Here is my <a href="cv/">CV</a>.</p>
"""

# (date, html). Newest first.
NEWS = [
    ("Oct 2026", 'Leading the acoustic analysis team on a <a href="projects/lpbf-acoustics/">laser powder bed fusion monitoring project</a>: we split hours of chamber audio into individual printed layers.'),
    ("Sep 2026", "Started my M.S. in Industrial &amp; Systems Engineering at UW–Madison and joined the FEAP Lab as a research assistant. I'm also the reader/grader for ISyE 320 (Simulation and Probabilistic Modeling) this fall."),
    ("Sep 2026", "Joined <b>NSF I-Corps Quantum+X</b> to explore where quantum sensing and computing could meet fusion research."),
    ("Jun 2026", 'Our paper <a href="publications/">“Federated Learning-Based Regression Framework to Predict Printed Line Width in Electrohydrodynamic Inkjet Printing”</a> was presented at <b>NAMRC 54</b> (MSEC 2026) and published in <i>Manufacturing Letters</i>.'),
    ("Jun 2026", 'Our perforation defect detection work won <b>2nd Place</b> at the IEOM Senior Capstone Design Competition in Milwaukee, after placing <b>3rd of 33 teams</b> in the IISE QCRE Data Challenge.'),
    ("Jun 2026", 'Started a summer research internship at Purdue LAMM with Prof. Martin Jun, working on <a href="projects/ded-acoustics/">acoustic monitoring for directed energy deposition</a> and <a href="projects/svm-calibration/">surround-view camera calibration</a>. I also led Python labs for the KIAT Data Analytics Program.'),
    ("Jun 2026", "Co-Entrepreneurial Lead for <b>NSF I-Corps BOOST</b>, interviewing people in nuclear operations about how they manage knowledge."),
    ("Apr 2026", '<a href="https://github.com/joannemiki57/IncidentCopilot">Incident Copilot</a> won <b>1st Place</b> at the UW–Madison LikeLion Hackathon, and <a href="https://github.com/joannemiki57/Polaris">Polaris</a> was a <b>finalist</b> at the UW–Madison Cursor Hackathon.'),
    ("Apr 2026", "Presented <b>OraQ</b>, an AI oral cancer pre-screening app, with the LikeLion Data Science Team. I built the data pipeline and the backend."),
    ("Sep 2025", "Arrived at UW–Madison as a visiting student and joined the FEAP Lab as an undergraduate researcher. Our team took <b>4th Prize</b> in the Plexus Challenge at the Engineering Makerthon."),
    ("May 2025", "Presented “Bicycle Lift Installation Optimization based on Spatial Information” at the Korean Society of Systems Engineering."),
    ("Nov 2024", "Our microfluidic sweat-sensing patch won <b>2nd Prize</b> in the Witeck field-based technical problem-solving project."),
]

ME = ["J. Yun", "Junghyun Yun", "Joanne Yun"]

PUBS = [
    {
        "key": "zhang2026federated",
        "year": "2026",
        "abbr": "Mfg. Letters",
        "thumb": "assets/img/projects/ehd_fl.jpg",
        "title": "Federated Learning-Based Regression Framework to Predict Printed Line Width in Electrohydrodynamic Inkjet Printing",
        "authors": ["Pengyu Zhang", "Junghyun Yun", "Hantang Qin"],
        "venue": "<em>Manufacturing Letters</em>, vol. 49, pp. 1298–1307. 54th SME North American Manufacturing Research Conference (NAMRC 54)",
        "date": "2026",
        "award": "",
        "abstract": "Accurate prediction of printed line width is essential to achieve dimensional precision and process stability in electrohydrodynamic (EHD) printing. However, training a reliable regression model requires large, diverse datasets that capture the full spectrum of process variability. In practice, data generated from different EHD systems or laboratories often exhibit domain-specific characteristics due to differences in environmental factors such as humidity, temperature, and equipment condition. These discrepancies, coupled with data privacy and ownership constraints, hinder the creation of centralized datasets for model development. To address this challenge, this study introduces a federated learning (FL)-based regression framework that enables collaborative model training across distributed EHD systems without exposing raw data. Each client trains a local regressor using its own process and imaging data, and a global model is periodically aggregated to integrate distributed knowledge while preserving confidentiality. Experimental results demonstrate that the developed FL framework effectively captures inter-system variability and achieves superior prediction accuracy compared with individual learning. Furthermore, transfer learning experiments confirm the framework's scalability to new inks and substrates. This work establishes a foundation for privacy-preserving, generalizable, and data-driven control in next-generation additive manufacturing systems.",
        "links": [
            ("DOI", "https://doi.org/10.1016/j.mfglet.2026.08.036"),
            ("Project", "projects/ehd-federated/"),
        ],
        "bibtex": """@article{zhang2026federated,
  title   = {Federated Learning-Based Regression Framework to Predict Printed Line Width in Electrohydrodynamic Inkjet Printing},
  author  = {Zhang, Pengyu and Yun, Junghyun and Qin, Hantang},
  journal = {Manufacturing Letters},
  volume  = {49},
  pages   = {1298--1307},
  year    = {2026},
  doi     = {10.1016/j.mfglet.2026.08.036}
}""",
        "selected": True,
    },
    {
        "key": "yun2026ieom",
        "year": "2026",
        "abbr": "IEOM 2026",
        "abbr_class": "alt",
        "thumb": "assets/img/projects/defect_poster.jpg",
        "title": "End-to-End Computer Vision Pipeline for Perforation Defect Detection and Classification in Industrial Imaging",
        "authors": ["Joanne Yun", "Hasnaa Ouidadi", "Khawlah Alharbi", "Pengyu Zhang", "Hantang Qin"],
        "venue": "Poster, <em>11th North American Conference on Industrial Engineering and Operations Management</em>, Milwaukee, WI",
        "date": "Jun 2026",
        "award": "2nd Place, IEOM Senior Capstone Design Competition",
        "abstract": "",
        "links": [
            ("Poster", "assets/pdf/IEOM2026_poster_Yun.pdf"),
            ("Project", "projects/perforation-defects/"),
        ],
        "bibtex": "",
        "selected": True,
    },
    {
        "key": "ouidadi2026perforation",
        "year": "In preparation",
        "abbr": "Manuscript",
        "abbr_class": "soft",
        "thumb": "assets/img/projects/defect_flow.jpg",
        "title": "Deep Learning-Based Perforation Defect Detection and Classification for Automated Industrial Inspection: An Industry Case Study",
        "authors": ["Hasnaa Ouidadi", "Khawlah Alharbi", "Pengyu Zhang", "Joanne Yun", "Hantang Qin"],
        "venue": "In preparation",
        "date": "",
        "award": "",
        "abstract": "",
        "links": [("Project", "projects/perforation-defects/")],
        "bibtex": "",
        "selected": False,
    },
    {
        "key": "yun2025bicycle",
        "year": "2025",
        "abbr": "KSSE 2025",
        "abbr_class": "soft",
        "thumb": "",
        "title": "Bicycle Lift Installation Optimization based on Spatial Information",
        "authors": ["Joanne Yun"],
        "venue": "Talk, <em>The Korean Society of Systems Engineering</em>, Korea",
        "date": "May 2025",
        "award": "",
        "abstract": "",
        "links": [],
        "bibtex": "",
        "selected": False,
    },
]

# Research projects: these get their own pages.
RESEARCH = [
    {
        "slug": "lpbf-acoustics",
        "title": "Listening to a Laser Powder Bed Fusion Print",
        "sub": "UW–Madison FEAP Lab · Sep 2026 to present",
        "img": "assets/img/projects/lpbf_spectrogram.jpg",
        "blurb": "Splitting hours of chamber audio into individual printed layers, as the first step toward predicting material properties of EUROFER97 steel from sound.",
        "tags": ["acoustics", "signal processing", "LPBF"],
        "meta": "UW–Madison, Flexible Electronics &amp; Additive Printing Lab · Advisor: Prof. Hantang Qin · Team lead, acoustic analysis",
        "body": """
<p>Laser powder bed fusion (LPBF) builds a metal part one thin layer at a time: a recoater blade spreads powder, the laser melts the cross-section, and the cycle repeats. A microphone in the build chamber hears all of it. The question behind this project is whether that sound can tell us something about the material being made. Before any of that, the audio has to be cut into layers, and on a multi-hour recording that has to be automatic.</p>

<div class="figure"><img src="../../assets/img/projects/lpbf_spectrogram.jpg" alt="Spectrogram of LPBF chamber audio for one layer"><figcaption>Chamber microphone spectrogram for a single layer, after cleaning.</figcaption></div>

<h3>What I built</h3>
<ul>
<li>A Python pipeline that isolates printing layers from LPBF chamber audio, supporting a funded project on in-situ material-property prediction for EUROFER97 steel.</li>
<li>Acoustic equalization, harmonic–percussive separation, and log-mel template matching to find recoater events, then layer boundaries from the energy change when the laser restarts.</li>
<li>A 5.2-hour recording segmented into <b>209 layer segments</b> and its shorter companion channel into <b>135</b>, exported as WAV clips with an Excel timing index and spot-checked by hand.</li>
<li>A video-side check: the chamber camera sees the laser, so brightness inside the build-plate region gives an independent laser-on/off signal.</li>
</ul>

<div class="figure"><img src="../../assets/img/projects/lpbf_template.jpg" alt="Equalized spectrogram of the recoater template"><figcaption>The recoater pass has a clear acoustic signature, which becomes a template for matching.</figcaption></div>

<div class="fig-row">
<div class="figure"><img src="../../assets/img/projects/lpbf_roi.jpg" alt="Camera frame with detected scan positions"><figcaption>Camera frame with the build-plate region and detected part positions.</figcaption></div>
<div class="figure"><img src="../../assets/img/projects/lpbf_layermap.jpg" alt="Numbered part map for layer 58"><figcaption>Part-by-part scan order mapped for one layer.</figcaption></div>
</div>

<div class="figure"><img src="../../assets/img/projects/lpbf_recoat.jpg" alt="Sequence of video frames during recoating"><figcaption>Video frames across a recoat, used to line the audio up with what the machine is doing.</figcaption></div>
""",
    },
    {
        "slug": "ded-acoustics",
        "title": "Acoustic Process Monitoring in Directed Energy Deposition",
        "sub": "Purdue LAMM · Summer 2026",
        "img": "assets/img/projects/ded_spectrogram.jpg",
        "blurb": "Separating what the laser, the powder feed, and the motion system each sound like, and finding a 7–8.5 kHz transient that only appears when the laser switches on.",
        "tags": ["acoustics", "DED", "synchronization"],
        "meta": "Purdue University, Laboratory for Advanced Multiscale Manufacturing · Prof. Martin Jun · Research intern",
        "body": """
<p>A directed energy deposition (DED) machine is loud, and most of that noise has nothing to do with the melt pool. To find a sound that actually belongs to the process, you need to know which subsystem is making which sound.</p>

<div class="figure"><img src="../../assets/img/projects/ded_spectrogram.jpg" alt="Spectrogram of a DED run against program time"><figcaption>Spectrogram of a DED run (0–8 kHz) against machine program time.</figcaption></div>

<h3>What I did</h3>
<ul>
<li>Analyzed a six-run subsystem-isolation study to separate laser, powder-feed, and motion contributions in the audio.</li>
<li>Aligned audio, video, and machine logs using oxygen readings, with a <b>0.17 s</b> alignment residual in the analyzed recordings.</li>
<li>Mapped G-code operations to machine-log timestamps and segmented the audio into contour, infill, traverse, and layer transition, so laser-on and laser-off runs of the same operation could be compared directly.</li>
<li>Found that apparent broadband "laser events" also showed up in the laser-off controls. Averaging over 45 laser-on edges revealed a <b>7–8.5 kHz transient</b> that is absent from the matching control, a candidate process signature for further study.</li>
</ul>

<div class="figure"><img src="../../assets/img/projects/ded_timefreq.jpg" alt="Waveform and spectrogram of a synchronized run"><figcaption>Waveform and spectrogram of one synchronized run.</figcaption></div>
""",
    },
    {
        "slug": "svm-calibration",
        "title": "Geometry-Based Surround-View Camera Calibration",
        "sub": "Purdue LAMM · Summer 2026",
        "img": "assets/img/projects/calib_grid.jpg",
        "blurb": "A targetless way to refine camera roll from known vehicle dimensions and image boundaries, plus work on a C++/OpenCV surround-view simulator.",
        "tags": ["computer vision", "calibration", "OpenCV"],
        "meta": "Purdue University, Laboratory for Advanced Multiscale Manufacturing · Prof. Martin Jun · Research intern",
        "body": """
<p>Surround-view systems stitch four fisheye cameras into a single bird's-eye view. If one camera is slightly rotated, the seams tear. Factory calibration uses printed targets; the goal here was to tighten calibration without them, so the system can keep itself calibrated on the road.</p>

<div class="figure"><img src="../../assets/img/projects/calib_grid.jpg" alt="Four fisheye views with projected ground grids"><figcaption>Projected ground grids on all four fisheye cameras, used to check the extrinsics.</figcaption></div>

<h3>What I did</h3>
<ul>
<li>Proposed and implemented a targetless calibration method that uses known vehicle dimensions and image boundaries to refine camera roll, narrowing the image-search region for online road calibration.</li>
<li>Implemented gradient-based boundary extraction and robust optimization in Python/OpenCV, compared calibration methods, and investigated systematic bias and poorly conditioned views.</li>
<li>Contributed to a C++/OpenCV surround-view simulator with interactive camera-pose switching, and ported a road-scene selection pipeline built on feature tracking and geometric outlier rejection.</li>
</ul>

<div class="fig-row">
<div class="figure"><img src="../../assets/img/projects/calib_ground.jpg" alt="Usable ground regions per camera"><figcaption>Which parts of each view are usable road surface.</figcaption></div>
<div class="figure"><img src="../../assets/img/projects/calib_sim.jpg" alt="Simulated fisheye front view"><figcaption>A simulated fisheye front view from the surround-view simulator.</figcaption></div>
</div>
""",
    },
    {
        "slug": "ehd-federated",
        "title": "Federated Learning for EHD Inkjet Printing",
        "sub": "UW–Madison FEAP Lab · 2025–2026 · Manufacturing Letters",
        "img": "assets/img/projects/ehd_fl.jpg",
        "blurb": "Predicting printed line width across eight printing systems without pooling their data. A model that scores R² = 0.983 at home can go negative on someone else's printer.",
        "tags": ["federated learning", "XGBoost", "additive manufacturing"],
        "meta": "UW–Madison, Flexible Electronics &amp; Additive Printing Lab · with Pengyu Zhang and Prof. Hantang Qin · <a href=\"https://doi.org/10.1016/j.mfglet.2026.08.036\">Paper (DOI)</a>",
        "body": """
<p>Electrohydrodynamic (EHD) inkjet printing uses an electric field to pull very fine lines of ink out of a nozzle. How wide the line comes out depends on voltage, frequency, duty ratio, standoff distance, and on the particular machine and room. Each lab has its own data and usually can't share it. Federated learning lets every lab train locally and share only model updates.</p>

<div class="fig-row">
<div class="figure"><img src="../../assets/img/projects/ehd_setup.jpg" alt="EHD printing setup schematic"><figcaption>EHD printing setup and how frequency changes line width.</figcaption></div>
<div class="figure"><img src="../../assets/img/projects/ehd_fl.jpg" alt="Federated learning server and clients diagram"><figcaption>Each printing system is a client; only model parameters go to the server.</figcaption></div>
</div>

<h3>My part</h3>
<ul>
<li>Built individual XGBoost regressors and data-processing pipelines for <b>8 printing-system clients</b> in a study reporting 1,185 experimental runs. These are the baseline the federated framework is compared against.</li>
<li>Showed that a strong within-client model (<b>R² = 0.983</b>) gave <b>negative R²</b> on four other clients when transferred. That cross-system failure is the motivation for the federated comparison.</li>
</ul>

<div class="figure"><img src="../../assets/img/projects/ehd_scatter.jpg" alt="Actual vs predicted line width for individual, centralized, and federated learning"><figcaption>Actual vs. predicted line width for individual, centralized, and federated learning. Figure from Zhang, Yun &amp; Qin, <i>Manufacturing Letters</i> 49 (2026), CC BY-NC-ND 4.0.</figcaption></div>
""",
    },
    {
        "slug": "perforation-defects",
        "title": "Perforation Defect Detection for Industrial Inspection",
        "sub": "UW–Madison FEAP Lab · 2025–2026 · IEOM 2nd Place · QCRE 3rd of 33",
        "img": "assets/img/projects/defect_poster.jpg",
        "blurb": "Labeling 900 of 25,000 production images, generating pseudo-labels for the rest, and training a detector that finds 93.4% of defect regions.",
        "tags": ["object detection", "pseudo-labeling", "Faster R-CNN"],
        "meta": "UW–Madison, Flexible Electronics &amp; Additive Printing Lab · co-led with postdoctoral researcher Hasnaa Ouidadi · Prof. Hantang Qin",
        "body": """
<p>An industry partner had about 25,000 unlabeled images of perforated material and needed defects found and classified automatically. Hand-labeling all of them was not an option, so most of the work went into deciding <i>which</i> images to label and how to label the rest automatically.</p>

<div class="figure"><img src="../../assets/img/projects/defect_poster.jpg" alt="IEOM 2026 poster"><figcaption>Our poster at IEOM 2026 in Milwaukee, which won 2nd Place in the Senior Capstone Design Competition. <a href="../../assets/pdf/IEOM2026_poster_Yun.pdf">PDF</a></figcaption></div>

<h3>What I did</h3>
<ul>
<li>Co-led the defect-inspection research and designed an annotation strategy of roughly <b>900 images</b> (informative plus random samples) out of 25,000.</li>
<li>Co-wrote the sampling and pseudo-labeling methods for the manuscript, and evaluated the adaptive-thresholding pseudo-labeler with component ablations and a six-parameter sensitivity analysis.</li>
<li>Under a center-based localization metric, the pipeline located <b>93.4% of 852 regions</b> across 213 images with 18 false boxes.</li>
<li>Reconstructed the Faster R-CNN training pipeline, reaching <b>85.0% AP / 97.6% AP50</b> on 178 validation images.</li>
</ul>

<div class="figure"><img src="../../assets/img/projects/defect_flow.jpg" alt="Adaptive thresholding pseudo-label flow"><figcaption>The pseudo-labeling flow: dual-stage detector, geometric filter, dot association, NMS, auto pseudo-label.</figcaption></div>

<div class="figure" style="max-width:520px;margin-left:auto;margin-right:auto"><img src="../../assets/img/projects/defect_f1.jpg" alt="Active learning accuracy gain chart"><figcaption>A second round of training with active-learning curation raised classifier micro-F1 (from the poster).</figcaption></div>

<div class="callout">Recognition: <b>3rd of 33 teams</b>, IISE QCRE Data Challenge 2026 · <b>2nd Place</b>, IEOM Senior Capstone Design Competition 2026</div>
""",
    },
]

# Smaller projects: grid cards, no page of their own.
BUILDS = [
    {"title": "Incident Copilot", "img": "assets/img/projects/build_incident.jpg", "icon": "fa-solid fa-life-ring", "sub": "1st Place · UW–Madison LikeLion Hackathon 2026",
     "text": "An incident-response console that walks raw logs through triage, root-cause hypotheses, evidence, and an action plan with human-in-the-loop gates. Built in a day by a team of three.",
     "tags": ["Next.js", "FastAPI", "SSE"], "url": "https://github.com/joannemiki57/IncidentCopilot"},
    {"title": "Polaris", "img": "assets/img/projects/build_polaris.jpg", "icon": "fa-solid fa-diagram-project", "sub": "Finalist · UW–Madison Cursor Hackathon 2026",
     "text": "Type a research question, get a knowledge graph grounded in real papers from OpenAlex, then expand nodes and chat with the papers.",
     "tags": ["React", "TypeScript", "Gemini"], "url": "https://github.com/joannemiki57/Polaris"},
    {"title": "OraQ", "icon": "fa-solid fa-tooth", "sub": "LikeLion Data Science Team · Spring 2026",
     "text": "Photograph the inside of your mouth and get an oral cancer risk estimate you can track over time. I owned data collection, preprocessing, and the whole backend.",
     "tags": ["backend", "CNN", "mobile"], "url": ""},
    {"title": "PCB Defect Detector", "icon": "fa-solid fa-microchip", "sub": "4th Prize · Plexus Challenge, UW–Madison Makerthon 2025",
     "text": "A Raspberry Pi board-inspection prototype. My idea: instead of collecting rare defect images, learn what each component looks like and flag parts that don't match.",
     "tags": ["Raspberry Pi", "computer vision"], "url": ""},
    {"title": "Solar Panel Anomaly Detection", "icon": "fa-solid fa-solar-panel", "sub": "Ajou University · with Korea Midland Power &amp; Kernelog",
     "text": "API-based telemetry acquisition for a solar-panel digital twin, and an anomaly-detection model on top of it.",
     "tags": ["digital twin", "anomaly detection"], "url": ""},
    {"title": "Microfluidic Sweat Patch", "icon": "fa-solid fa-droplet", "sub": "2nd Prize · Witeck project 2024 · team lead",
     "text": "A PDMS sweat-extraction patch with colorimetric pH sensing, plus an image-based algorithm that turns sensor color into a pH value.",
     "tags": ["microfluidics", "image analysis"], "url": ""},
    {"title": "Virtual Aircraft Assembly", "icon": "fa-solid fa-plane", "sub": "Ajou University · 2025",
     "text": "A Unity environment for practicing jet-engine assembly and disassembly in 3D.",
     "tags": ["Unity", "C#"], "url": ""},
    {"title": "Bicycle Lift Siting", "icon": "fa-solid fa-map-location-dot", "sub": "Korean Society of Systems Engineering · 2025",
     "text": "Where should a city put bicycle lifts on steep roads? An optimization using QGIS and public spatial data.",
     "tags": ["QGIS", "optimization"], "url": ""},
    {"title": "Trips", "img": "assets/img/projects/build_trips.jpg", "icon": "fa-solid fa-images", "sub": "Personal project · iOS",
     "text": "A SwiftUI app that turns a trip's camera roll into a curated album once the trip is over.",
     "tags": ["Swift", "SwiftUI"], "url": "https://github.com/joannemiki57/Trips"},
]

MADISON = [
    ("assets/img/madison/capitol.jpg", "The Capitol"),
    ("assets/img/madison/mendota.jpg", "Lake Mendota"),
    ("assets/img/madison/state-street.jpg", "State Street"),
    ("assets/img/madison/game-day.jpg", "Game day"),
]

CV_SECTIONS = [
    ("Education", [
        ("University of Wisconsin–Madison", "Sep 2026 – May 2027 (expected)", "M.S., Industrial &amp; Systems Engineering", []),
        ("University of Wisconsin–Madison", "Sep 2025 – May 2026", "Visiting International Student Program, Industrial &amp; Systems Engineering", []),
        ("Ajou University, Suwon, South Korea", "Mar 2023 – Aug 2026", "B.S., Industrial Engineering · Class rank 1/139 · GPA 4.26/4.5 · Dean's List", []),
    ]),
    ("Research Experience", [
        ("FEAP Lab, UW–Madison", "Sep 2025 – present", "Research Assistant (from Sep 2026), Undergraduate Researcher (Sep 2025 – May 2026) · Prof. Hantang Qin",
         ["Acoustic monitoring for laser powder bed fusion", "Cross-system line-width prediction in EHD inkjet printing", "Industrial surface-defect detection"]),
        ("Laboratory for Advanced Multiscale Manufacturing, Purdue University", "Jun – Aug 2026", "Research Intern · Prof. Martin Jun",
         ["Acoustic process monitoring in directed energy deposition", "Geometry-based surround-view camera calibration"]),
        ("New Industrial Convergence R&amp;D Lab, Ajou University", "Mar 2023 – Aug 2025", "Undergraduate Research Intern · Prof. Jooyeon Lee",
         ["Solar-panel digital-twin telemetry and anomaly detection", "Microfluidic sweat-sensing patch"]),
    ]),
    ("Teaching", [
        ("Reader/Grader, ISyE 320: Simulation and Probabilistic Modeling", "Sep 2026 – present", "UW–Madison · Prof. Qiaomin Xie · sole grader for about 80 students", []),
        ("Teaching Support, KIAT Data Analytics Program", "Jun – Aug 2026", "Purdue · hands-on Python labs and office hours for 90+ visiting scholars", []),
    ]),
    ("Honors &amp; Awards", [
        ("2nd Place, IEOM Senior Capstone Design Competition", "2026", "", []),
        ("3rd of 33 teams, IISE QCRE Data Challenge", "2026", "", []),
        ("1st Place, UW–Madison LikeLion Hackathon (Incident Copilot)", "2026", "", []),
        ("Finalist, UW–Madison Cursor Hackathon (Polaris)", "2026", "", []),
        ("4th Prize, Plexus Challenge, UW–Madison Engineering Makerthon", "2025", "", []),
        ("2nd Prize, Witeck Field-based Technical Problem Solving Project", "2024", "", []),
        ("3rd Prize, Seongnam City Public Data Analysis Idea Contest", "2024", "", []),
        ("1st Prize, 10th Ajou Hidden Champion Contest", "2023", "", []),
        ("Ajou University scholarships; Guwon Scholarship Foundation", "2023 – 2025", "", []),
    ]),
    ("Leadership &amp; Service", [
        ("Co-Entrepreneurial Lead, NSF I-Corps BOOST", "Summer 2026", "Customer discovery on knowledge management in nuclear operations", []),
        ("Participant, NSF I-Corps Quantum+X", "Sep 2026 – present", "", []),
        ("Public Relations Manager, LikeLion US at UW–Madison", "2026 – present", "", []),
        ("Vice President (prev. Treasurer), WAI Career Organization, Ajou IE", "Sep 2023 – Aug 2024", "Organized career talks for 100+ students", []),
        ("Volunteer Educator, Hyundai Motor Group H-Jump School", "Mar – Nov 2024", "100+ hours teaching English and math", []),
    ]),
    ("Skills", [
        ("Programming", "", "Python, C++, SQL, NumPy, pandas, SciPy, Git, CMake", []),
        ("Machine learning &amp; vision", "", "PyTorch, scikit-learn, XGBoost, Detectron2, OpenCV", []),
        ("Signal processing", "", "STFT, log-mel features, acoustic equalization, template matching, event averaging, audio/video/log synchronization", []),
    ]),
]

# =====================================================================
# TEMPLATES
# =====================================================================

NAV = [("about", ""), ("publications", "publications/"), ("projects", "projects/"), ("news", "news/"), ("cv", "cv/")]


def esc(s):
    return html.escape(s, quote=True)


def social(p):
    return f"""<div class="social-icons">
<a href="mailto:{SITE['email']}" title="email"><i class="fa-solid fa-envelope"></i></a>
<a href="{SITE['scholar']}" title="Google Scholar"><i class="ai ai-google-scholar"></i></a>
<a href="{SITE['github']}" title="GitHub"><i class="fa-brands fa-github"></i></a>
<a href="{SITE['linkedin']}" title="LinkedIn"><i class="fa-brands fa-linkedin"></i></a>
</div>"""


def page(title, active, p, body, description=""):
    """p is the relative prefix back to the site root ('' or '../' etc.)."""
    act = ' class="active"'
    nav = "\n".join(
        f'<li><a href="{p}{href}"{act if name == active else ""}>{name}</a></li>' for name, href in NAV
    )
    left = social(p) if active == "about" else (
        f'<a class="navbar-brand" href="{p}"><span class="first">{SITE["first"]}</span> {SITE["last"]}</a>'
    )
    full_title = f"{SITE['first']} {SITE['last']}" if active == "about" else f"{title} | {SITE['first']} {SITE['last']}"
    desc = description or "Joanne Yun: M.S. student in Industrial & Systems Engineering at UW–Madison working on machine learning for manufacturing and acoustic process monitoring."
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full_title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="author" content="{esc(SITE['full'])}">
<meta property="og:title" content="{esc(full_title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="https://joannemiki57.github.io/assets/img/prof_pic.jpg">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2218%22 fill=%22%23c5050c%22/><text x=%2250%22 y=%2268%22 font-size=%2252%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22Arial%22 font-weight=%22bold%22>JY</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/academicons/1.9.4/css/academicons.min.css">
<link rel="stylesheet" href="{p}assets/css/main.css">
<script src="{p}assets/js/main.js"></script>
</head>
<body>
<header class="navbar">
<div class="container">
{left}
<button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false"><i class="fa-solid fa-bars"></i></button>
<ul class="nav-links">
{nav}
<li><button class="theme-toggle" title="Toggle dark mode" aria-label="Toggle dark mode"><i class="fa-solid fa-moon"></i><i class="fa-solid fa-sun"></i></button></li>
</ul>
</div>
</header>
<main class="container">
{body}
</main>
<footer>© Copyright 2026 {esc(SITE['full'])}. Layout inspired by the <a href="https://github.com/alshedivat/al-folio">al-folio</a> theme. Last updated: {SITE['updated']}.</footer>
</body>
</html>
"""


def news_table(items):
    rows = "\n".join(f"<tr><th>{d}</th><td>{t}</td></tr>" for d, t in items)
    return f'<table class="news-table">{rows}</table>'


def authors_html(authors):
    out = []
    for a in authors:
        out.append(f'<span class="me">{a}</span>' if a in ME else a)
    if len(out) == 1:
        return out[0]
    if len(out) == 2:
        return f"{out[0]} and {out[1]}"
    return ", ".join(out[:-1]) + ", and " + out[-1]


def pub_item(pub, p):
    links = []
    if pub["abstract"]:
        links.append(f'<button data-toggle="abs-{pub["key"]}">Abs</button>')
    for label, href in pub["links"]:
        h = href if href.startswith("http") else p + href
        links.append(f'<a href="{h}">{label}</a>')
    if pub["bibtex"]:
        links.append(f'<button data-toggle="bib-{pub["key"]}">Bib</button>')
    thumb = f'<img class="pub-thumb" src="{p}{pub["thumb"]}" alt="" loading="lazy">' if pub.get("thumb") else ""
    award = f'<div class="award"><i class="fa-solid fa-trophy"></i> {pub["award"]}</div>' if pub["award"] else ""
    date = f", {pub['date']}" if pub["date"] and pub["date"] not in pub["venue"] else ""
    abs_div = f'<div class="abstract" id="abs-{pub["key"]}">{esc(pub["abstract"])}</div>' if pub["abstract"] else ""
    bib_div = f'<div class="bibtex" id="bib-{pub["key"]}"><pre>{esc(pub["bibtex"])}</pre></div>' if pub["bibtex"] else ""
    return f"""<li><div class="pub">
<div class="abbr-col"><span class="abbr {pub.get('abbr_class', '')}">{pub['abbr']}</span>{thumb}</div>
<div class="body">
<div class="title">{pub['title']}</div>
<div class="author">{authors_html(pub['authors'])}</div>
<div class="periodical">{pub['venue']}{date}</div>
{award}
<div class="links">{''.join(links)}</div>
{abs_div}{bib_div}
</div></div></li>"""


def build_about():
    p = ""
    selected = "\n".join(pub_item(x, p) for x in PUBS if x["selected"])
    gallery = "\n".join(
        f'<figure><img src="{src}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>' for src, cap in MADISON
    )
    body = f"""
<div class="post-header">
<h1 class="post-title"><span class="first">{SITE['first']}</span> {SITE['last']}</h1>
<p class="post-description">Junghyun (Joanne) Yun · M.S. student, Industrial &amp; Systems Engineering, UW–Madison</p>
</div>
<article class="clearfix">
<div class="profile">
<img src="assets/img/prof_pic.jpg" alt="Joanne Yun">
<div class="caption">KSEA Midwest Regional Conference, Chicago</div>
</div>
<div class="about-text">{ABOUT_HTML}</div>
</article>

<h2 class="section-title"><a href="news/">news</a></h2>
{news_table(NEWS[:5])}

<h2 class="section-title"><a href="publications/">selected publications</a></h2>
<ol class="bibliography">{selected}</ol>

<h2 class="section-title">around madison</h2>
<p class="post-description">A few photos from my first year here.</p>
<div class="gallery">{gallery}</div>
"""
    write("index.html", page("about", "about", p, body))


def build_publications():
    p = "../"
    parts = []
    year = None
    for pub in PUBS:
        if pub["year"] != year:
            if year is not None:
                parts.append("</ol>")
            year = pub["year"]
            parts.append(f'<h2 class="year-heading">{year}</h2><ol class="bibliography">')
        parts.append(pub_item(pub, p))
    parts.append("</ol>")
    body = f"""
<div class="post-header">
<h1 class="post-title">publications</h1>
<p class="post-description">Papers, posters, and talks. Also on <a href="{SITE['scholar']}">Google Scholar</a>.</p>
</div>
{''.join(parts)}
"""
    write("publications/index.html", page("publications", "publications", p, body))


def build_projects():
    p = "../"
    hcards = "\n".join(
        f"""<a class="hcard" href="{r['slug']}/">
<div class="thumb" style="background-image:url('{p}{r['img']}')"></div>
<div class="card-body">
<h3 class="card-title">{r['title']}</h3>
<p class="card-sub">{r['sub']}</p>
<p class="card-text">{r['blurb']}</p>
<div class="card-tags">{''.join(f'<span class="tag">{t}</span>' for t in r['tags'])}</div>
</div></a>"""
        for r in RESEARCH
    )
    vcards = []
    for b in BUILDS:
        thumb = (f'<div class="img-thumb" style="background-image:url(\'{p}{b["img"]}\')"></div>'
                 if b.get("img") else f'<div class="icon-thumb"><i class="{b["icon"]}"></i></div>')
        tag = "a" if b["url"] else "div"
        href = f' href="{b["url"]}"' if b["url"] else ""
        gh = ' <i class="fa-brands fa-github" style="font-size:0.9rem"></i>' if "github.com" in b["url"] else ""
        vcards.append(f"""<{tag} class="vcard"{href}>
{thumb}
<div class="card-body">
<h3 class="card-title">{b['title']}{gh}</h3>
<p class="card-sub">{b['sub']}</p>
<p class="card-text">{b['text']}</p>
<div class="card-tags">{''.join(f'<span class="tag">{t}</span>' for t in b['tags'])}</div>
</div></{tag}>""")
    body = f"""
<div class="post-header">
<h1 class="post-title">projects</h1>
<p class="post-description">Research first, then things I built for fun, for class, or in a hackathon.</p>
</div>
<h2 class="section-title">research</h2>
<div class="proj-list">{hcards}</div>
<h2 class="section-title">builds &amp; side projects</h2>
<div class="grid">{''.join(vcards)}</div>
"""
    write("projects/index.html", page("projects", "projects", p, body))

    for r in RESEARCH:
        pp = "../../"
        body = f"""
<div class="post-header">
<h1 class="post-title">{r['title']}</h1>
<p class="post-description">{r['sub']}</p>
</div>
<p class="project-meta">{r['meta']}</p>
<div class="content">{r['body']}</div>
<a class="back-link" href="../">← all projects</a>
"""
        write(f"projects/{r['slug']}/index.html", page(r["title"], "projects", pp, body, r["blurb"]))


def build_news():
    p = "../"
    # Links inside news items are written relative to the site root.
    items = [(d, t.replace('href="projects/', f'href="{p}projects/').replace('href="publications/', f'href="{p}publications/')) for d, t in NEWS]
    body = f"""
<div class="post-header"><h1 class="post-title">news</h1></div>
{news_table(items)}
"""
    write("news/index.html", page("news", "news", p, body))


def build_cv():
    p = "../"
    secs = []
    for name, items in CV_SECTIONS:
        rows = []
        for what, when, detail, bullets in items:
            rows.append(f'<div class="cv-item"><span class="what">{what}</span><span class="when">{when}</span></div>')
            if detail:
                rows.append(f'<p class="cv-detail">{detail}</p>')
            if bullets:
                rows.append("<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>")
        secs.append(f'<section class="cv-section"><h2>{name}</h2>{"".join(rows)}</section>')
    body = f"""
<div class="cv-head">
<div class="post-header"><h1 class="post-title">cv</h1><p class="post-description">Last updated October 2026.</p></div>
<a class="pdf-btn" href="{p}{SITE['cv_pdf']}" target="_blank" rel="noopener"><i class="fa-solid fa-file-pdf"></i> PDF</a>
</div>
<object class="pdf-frame" data="{p}{SITE['cv_pdf']}#view=FitH" type="application/pdf">
<p style="padding:16px">Your browser can't show the PDF here. <a href="{p}{SITE['cv_pdf']}">Download the CV</a> instead.</p>
</object>
{''.join(secs)}
"""
    write("cv/index.html", page("cv", "cv", p, body))


def write(rel, text):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote", rel)


if __name__ == "__main__":
    build_about()
    build_publications()
    build_projects()
    build_news()
    build_cv()
    # GitHub Pages: serve files as-is (no Jekyll processing of the _build folder).
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
