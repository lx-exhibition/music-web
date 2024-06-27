// 参考：https://github.com/tsparticles/vue3
// 如：需要查找 @tsparticles/slim 用法时，参考：
// https://particles.js.org/docs/classes/tsParticles_Engine.Options_Classes_Background_Background.Background.html
export let conf_effect = {
    background: {
        // image: "url('https://particles.js.org/images/background3.jpg')",
        // image: "url('https://sex.nyan.xyz/api/v2/img?r18=true&author_uuid=66371932&author_uuid=70395770&author_uuid=17516104&author_uuid=14496985&author_uuid=13835102&author_uuid=1642433&author_uuid=23040640')",
    },
    fpsLimit: 120,
    interactivity: {
        events: {
            onClick: {
                enable: true,
                mode: 'push'
            },
            onHover: {
                enable: true,
                mode: 'repulse'
            },
        },
        modes: {
            bubble: {
                distance: 400,
                duration: 2,
                opacity: 0.8,
                size: 40
            },
            push: {
                quantity: 4
            },
            repulse: {
                distance: 200,
                duration: 0.4
            }
        }
    },
    particles: {
        color: {
            value: '#000000'
        },
        links: {
            color: '#000000',
            distance: 150,
            enable: true,
            opacity: 0.5,
            width: 1
        },
        move: {
            direction: 'none',
            enable: true,
            outModes: 'bounce',
            random: false,
            speed: 6,
            straight: false
        },
        number: {
            density: {
                enable: true,
            },
            value: 80
        },
        opacity: {
            value: 0.5
        },
        shape: {
            type: 'circle'
        },
        size: {
            value: { min: 1, max: 3 }
        }
    },
    detectRetina: true
}