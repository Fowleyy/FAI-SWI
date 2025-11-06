let currentYear = new Date().getFullYear();
let currentMonth = new Date().getMonth() + 1;
let latestData = null;

async function loadCalendar(year, month, animateDir) {
    const response = await fetch(`/Calendar/GetMonth?year=${year}&month=${month}`);
    const data = await response.json();
    latestData = data;
    currentYear = data.year;
    currentMonth = data.month;
    renderCalendar(data, animateDir);
    renderEvents(null);
}


function renderCalendar(data, animateDir) {
    document.getElementById('calendar-title').innerText = `${data.monthName} ${data.year}`;
    // výpočet mřížky jako dříve
    let firstDayOfWeek = new Date(data.year, data.month-1, 1).getDay();
    if (firstDayOfWeek === 0) firstDayOfWeek = 7;

    const weeks = Math.ceil((firstDayOfWeek-1 + data.daysInMonth)/7);
    const grid = Array.from({length: weeks}, () => Array(7).fill(null));
    let day = 1;
    for(let w=0; w<weeks; w++) {
        for(let d=0; d<7; d++) {
            const calendarCellIndex = w*7 + d;
            if(calendarCellIndex >= firstDayOfWeek-1 && day <= data.daysInMonth) {
                grid[w][d] = day++;
            }
        }
    }
    const columns = Array.from({length:7}, (_,d)=> grid.map(week=>week[d]));
    const dayNames = ['Po','Út','St','Čt','Pá','So','Ne'];
    let html = `<div class="vertical-calendar">`;
    for (let col = 0; col < 7; col++) {
        html += `<div class="calendar-col">`;
        for(let row = 0; row < weeks; row++) {
            const aktDay = columns[col][row];
            if (!aktDay) {
                html += `<div class="calendar-rect empty"></div>`;
                continue;
            }
            const eventsToday = data.events.filter(ev=>ev.day===aktDay);
            const isToday = aktDay === new Date().getDate() && 
                data.month === (new Date().getMonth()+1) && 
                data.year === new Date().getFullYear();
            html += `<div class="calendar-rect${isToday ? " today" : ""}${eventsToday.length ? " has-events":""}" data-day="${aktDay}">
                        <div class="rect-date">${dayNames[col]}<br><strong>${aktDay}</strong></div>
                        ${eventsToday.length ? `<div class="rect-events">${eventsToday.map(ev=>`${ev.title}`).join('<br>')}</div>` : ""}
                    </div>`;
        }
        html += `</div>`;
    }
    html += `</div>`;

    const wrap = document.getElementById('calendar-anim-wrap');
    if (animateDir){
        wrap.classList.remove('slide-left','slide-right');
        void wrap.offsetWidth;
        wrap.classList.add(animateDir);
        setTimeout(()=>{
            wrap.innerHTML = html;
            wrap.classList.remove('slide-left','slide-right');
            attachDayClicks();
        }, 300);
    } else {
        wrap.innerHTML = html;
        attachDayClicks();
    }
}


function attachDayClicks(){
    document.querySelectorAll('.bubble-day[data-day]').forEach(el => {
        el.onclick = function() {
            let day = Number(this.getAttribute('data-day'));
            renderEvents(day);
            document.querySelectorAll('.bubble-day.selected').forEach(e=>e.classList.remove('selected'));
            this.classList.add('selected');
        };
    });
}

function renderEvents(day){
    const wrap = document.getElementById('event-list-wrap');
    if (!day) {
        wrap.innerHTML = "";
        return;
    }
    const events = latestData.events.filter(ev => ev.day === day);
    let html = `<h3>Události dne ${day}.${latestData.month}.${latestData.year}</h3>`;
    if (events.length) {
        html += "<ul>";
        for (const ev of events) {
            html += `<li><b>${ev.title}</b> - ${ev.start} - ${ev.end}</li>`;
        }
        html += "</ul>";
    } else {
        html += `<p>Žádné události pro tento den.</p>`;
    }
    wrap.innerHTML = html;
}

document.getElementById('prevBtn').onclick = () => {
    let y = currentYear, m = currentMonth - 1;
    if (m < 1) { m = 12; y--; }
    loadCalendar(y, m, 'slide-right');
};
document.getElementById('nextBtn').onclick = () => {
    let y = currentYear, m = currentMonth + 1;
    if (m > 12) { m = 1; y++; }
    loadCalendar(y, m, 'slide-left');
};

window.addEventListener('DOMContentLoaded',()=>{
    loadCalendar(currentYear, currentMonth);
});
