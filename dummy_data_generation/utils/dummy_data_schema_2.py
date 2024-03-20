import datetime


azure_blob_token = "sv=2022-11-02&ss=bfqt&srt=sco&sp=r&se=2024-12-31T12:27:34Z&st=2024-02-12T04:27:34Z&spr=https&sig=fOf%2Fsnurp420W8P%2BPxPcbIR56eLCGJ8pu4OjXiWj8cY%3D"
azure_blob_cover = "https://radowski.blob.core.windows.net/cover/<blob_name>"
azure_blob_book = "https://radowski.blob.core.windows.net/book/<blob_name>"
azure_blob_poem = "https://radowski.blob.core.windows.net/poem/<blob_name>"

libro_i_cover = azure_blob_cover.replace("<blob_name>", "libro_i.png")
libro_ii_cover = azure_blob_cover.replace("<blob_name>", "libro_ii.png")
poemas_para_mi_cover = azure_blob_cover.replace("<blob_name>", "poemas_para_mi.png")
libro_i_pdf = azure_blob_book.replace("<blob_name>", "libro_i.pdf")
libro_ii_pdf = azure_blob_book.replace("<blob_name>", "libro_i.pdf")
poemas_para_mi_pdf = azure_blob_book.replace("<blob_name>", "poemas_para_mi.pdf")
libro_i__book_i_pdf = azure_blob_book.replace("<blob_name>", "libro_i__book_i.pdf")
libro_ii__book_ii_pdf = azure_blob_book.replace("<blob_name>", "libro_ii__book_ii.pdf")
poemas_para_mi__poems_for_me_pdf = azure_blob_book.replace(
    "<blob_name>", "poemas_para_mi__poems_for_me.pdf"
)

content_book_ii = [
    {
        "poem_id": 1,
        "name": "dios",
        "title": "Dios",
        "dedication": None,
        "body": "No me sanes.\nQuiero la tristeza,\nquiero la depresión;\nson mis musas,\nno te las lleves.\nNo me llenes,\nestoy tan lleno,\nque no acepto más.\nSiento arcadas\n\ncuando me hablan de propósitos.\nQuisiera vomitar,\ndejar mi mente en blanco,\nignorarlo todo\ny —tal vez— ser feliz",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 2,
        "name": "identidad",
        "title": "Identidad",
        "dedication": None,
        "body": "Explora la tormenta.\nTócate y siente\ncomo todo es\nviento, arena y mugre;\nuna temporada seca,\notra húmeda.\nEres un péndulo\nque va y viene\nentre llanto e ira;\na veces asceta,\na veces pecadora.\nDe cálida a fría\nte revuelves a ti misma.\nNunca constante,\ncada vez más pesada\nte cuesta oscilar\n¿Qué eres?\nNo el tú;\nsino la infinita suma\nde lo que te rodea:\nimpulsos finitos,\nvoluntades ajenas.\nCuando te detengas,\nen equilibrio,\nte darás cuenta.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 3,
        "name": "spica",
        "title": "Spica",
        "dedication": None,
        "body": "Tú,\nartista y musa,\ndicotomía imposible.\nEntre tu culto y lo celestial,\nprefiero la condena.\nMártir por ti,\nque velada\nentre el cielo y la tierra,\nacoges bajo tu sombra \na los inconformes.\nEres para los hastiados \ndel alba y del crepúsculo\nla salvación de lo cotidiano,\nnuestro eclipse eterno.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 4,
        "name": "moral",
        "title": "Moral",
        "dedication": None,
        "body": "Siempre se puede empeorar,\ncaer más hondo.\nLa luz al final del túnel queda atrás\ny te preguntas:\n¿alguna vez tocaré fondo?\nSe cae por tanto tiempo \nque más arriba o más abajo\nno tiene sentido;\nmejor o peor no hace diferencia.\nPiensas:\n¿qué debo hacer?\n―No hagas.\nSé, existe.\nDisfruta tu maldad, tu bondad,\nlo que seas;\ncomo sea,\npronto\nchocarás con la sima.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 5,
        "name": "exhortacion",
        "title": "Exhortación",
        "dedication": None,
        "body": "Amor, desastre.\nEntre todos los desiertos\nel cactus pica al sol,\nsangra y quema la tierra.\nLas sandalias de la esfinge\nno la protegen de las llamas.\nAbandonadas\n―poesía y música―\nenterradas entre dunas.\nAquellos que lograron salir\nfueron alcanzados por la sombra.\nMiles de notas, ritmos y acordes\napagados por una tormenta de arena,\ncomo lluvia de balas,\nun genocidio artístico.\nA todos se les da una vida,\npero quiénes pueden llegar a ser inmortales.\nEscribe, talla, grita, graba.\nArtista, tus días están contados.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 6,
        "name": "voz_de_escritor",
        "title": "Voz de Escritor",
        "dedication": None,
        "body": "Encontré mi voz de escritor.\nEs gutural,\n―apagada y rasposa―\nllena de pesimismo.\n\nProclama:\n—La ignorancia te hace feliz.\n\nPor eso \ncuando te llame\nignórame \ny ve\nhacia donde el ruido blanco\nopaque mi voz.\n\nSiempre que te invite,\ncon una mirada derrotista,\na reflexionar\nsobre la vida,\ntápate los ojos\ny aléjate de mí.\n\n¿Pero, por qué?\nSigues leyendo.\n\nSigue mi voz\nte libraré de la felicidad.\n\nDesde un rincón\nte llamo a la sombra\ndonde todo es conocimiento.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 7,
        "name": "derrotismo",
        "title": "Derrotismo",
        "dedication": None,
        "body": "La vida empieza a mitad de camino\ncuando decides entre \nser el fruto más rojo en la copa\no regresar y no germinar.\nDecidí regresar, no serlo;\ndescender en la jerarquía.\nAdvertir, convencer a los demás\nde la inminente trampa:\narriba sólo los esperaba ser devorados\no ser ignorados;\neventualmente caer y pudrirse.\nDos caminos que llevan\na la misma fosa de estiércol\npara nutrir nuevamente el ciclo.\nNo quise más esfuerzo en vano\nasí que encontré las raíces,\nen lo más profundo.\nAcabado, me ahogué en la tierra\ny no tuve más pretensiones \nde ver el sol nuevamente.\nInundé de lágrimas aquel árbol seco y fatigado.\nDescubrí que\nlas penitencias acarreadas por el conocimiento \nson la soledad y la tristeza,\nel fracaso.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 8,
        "name": "utopia_de_ratas",
        "title": "Utopía de Ratas",
        "dedication": None,
        "body": "En el pináculo del desarrollo,\nmanos plásticas moldean la moral:\nLo masculino \nes forzado a lo femenino,\nque a su vez \nmarcha a su encuentro;\nen el centro se unen\ny desconcertados,\nellos mismos\nya no son.\nAlienados quieren llorar,\nno pueden;\nno hay emociones,\nsolo autómatas\nreaccionando a estímulos.\nEl amor, el odio;\nlas ambiciones, lo humano:\nconstrucciones sociales,\ndefectos del sistema.\nEl poder vence a la competencia\ny las jerarquías, corruptas,\nse vienen abajo.\nSe culpa a izquierda, a derecha;\nal Diablo, a Dios.\nEllos hace rato se volvieron indiferentes.\nPor otro lado, \nBaco se embriaga\ny disfruta el panorama:\n\nposapocalíptico, posmoderno;\nsin roles, sin identidad.\nLa anarquía anhelada:\nUna utopía de ratas.",
        "cover_url": libro_ii_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 9,
        "name": "reflexion_ii",
        "title": "Reflexión II",
        "dedication": None,
        "body": "Eludir lo inexorable\nes hablar de Dios.\nHablar de Dios es \npensar fuera del tiempo.\nPensar fuera del tiempo\nes soñar.\nSoñar es fantasear\nque los problemas de la vida\nse esfuman escribiendo.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 10,
        "name": "reflexion_iii",
        "title": "Reflexión III",
        "dedication": None,
        "body": "El artista no está en la obra,\nel artista está en el alma:\nentre la mente y el corazón,\npor los pulmones,\ndebajo del esternón;\ndonde el cigarro,\ndespués de cada calada,\ndeja una brasa encendida.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 11,
        "name": "reflexion_iv",
        "title": "Reflexión IV",
        "dedication": None,
        "body": "De noche \nen la playa\nel humo se disipa \nde forma mágica;\nadquiere otra actitud,\ntrata de imitar la serenidad del mar.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 12,
        "name": "reflexion_xii",
        "title": "Reflexión XII",
        "dedication": None,
        "body": "Oscilo entre lo malo y lo peor;\nno ser la mejor versión de mí mismo,\ny no querer serlo.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 13,
        "name": "no_es_suficiente",
        "title": "No es Suficiente",
        "dedication": None,
        "body": "Es curioso\nque no ser la mejor\nversión de ti mismo\nte haga malo.\n\nY no querer serlo\nte vuelva peor.\n\nLo desconcertante \nes que \npara ser bueno\nno basta solo con querer serlo.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 14,
        "name": "checa",
        "title": "Checa",
        "dedication": None,
        "body": "El primer paso\npara superar una adicción\nes aceptarla.\n\nNo se puede disimular\nuna borrachera\ncreyendo estar sobrio.\n\nPara superarte\ndebo aceptar\nque hay partes tuyas\nque no puedo olvidar.\n\nY no es la obsesión por ti,\nsino de lo que representas:\n\nLa idealización de una mujer;\nla musa perfecta.\n\nEl eterno capricho\nde querer\nlo que no puedo alcanzar.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 15,
        "name": "odio",
        "title": "Odio",
        "dedication": None,
        "body": "Me raparé las cejas\ny rasgaré mis prendas;\ny vuelto un completo asceta,\nhermético,\ncerraré la llave de mi alma.\nNo más efluvios de emociones;\nestancadas,\nme volverán carroña.\nSarnoso y callejero\naullaré a la luna\ny sin decoro mostraré indulgencia\npor mi propia debilidad.\n\nNo hay piedad\nen la sabiduría.\nNo hay sabiduría\nen el cansancio;\ntan aburrido de lo común,\ntan cansado del fracaso.\n\nSin historias\nlo mío son palabras recurrentes,\nfrases vagamente unidas;\ncolores intensos\nque abstrajeron todo a figuras,\nla búsqueda de un significado\nque me lleva a la nada,\nforzar un pensamiento\nvulgarizando el intelecto;\nel odio por mí mismo.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 16,
        "name": "ella",
        "title": "Ella",
        "dedication": None,
        "body": "La amaste, a tu manera.\nBajo yugo desigual\nquebraste su cuello.\nY con juramentos\nprometiste cambio,\npero no de tu parte.\nLa engañaste\ny su fe ciega exacerbó su enajenación.\nDe artista a musa\ncambió su mirada:\nsu brillo, sus ojos.\nSe convirtió en tu modelo.\nTransfigurada,\nla consagraste a tu altar\njunto a las Pléyades\ndonde hoy reposa\ndespojada de su cuerpo;\nque, sepultado por el tiempo,\nsin cruz ni epitafio,\nfue olvidado.\n¿Descansará en paz?\n¿Quién era ella?\nLa novia de …",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 17,
        "name": "media_de_lucky_rojo",
        "title": "Media de Lucky Rojo",
        "dedication": "Mångata",
        "body": "Un cigarro.\nHablamos del amor y del alma.\nNo los conocemos, ¿quién sí?\nSin embargo, habló de su ex\ny yo de la que nunca he tenido.\n\nDos cigarros.\nHablamos de la otredad:\ntodos se conocen,\npero nadie entiende a nadie.\n—Jamás seremos amigos realmente.\n—No pretendo que lo seamos.\n\nTres cigarros.\nRecurrió a los golpes,\nignoró palabras.\nPuños que hablan\nde resentimientos añejos.\nYo solo observo.\n\nCuatro cigarros.\nPalabras por humo.\nMatamos el tiempo,\nquemamos tabaco.\nNos miramos, nos reímos;\nmiramos al cielo,\nexhalamos.\n\nCinco cigarros.\n—El último es sagrado.\n\nSilencio,\nsímbolo de nuestra amistad.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 18,
        "name": "reflexion_ix",
        "title": "Reflexión IX",
        "dedication": "mi fe",
        "body": "“Más sabe el diablo\npor viejo\nque por diablo”.\nSi la sabiduría\nque solo los eones\npueden traer\nno lo han movido hacia un cambio,\n¿por qué debería yo\nbuscar virtud\nen la santidad?",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]
content_book_i = [
    {
        "poem_id": 19,
        "name": "nostalgia",
        "title": "Nostalgia",
        "dedication": None,
        "body": "Recuerdo…\nlos buenos tiempos pasados\ncomo pinceladas opacas\nsobre un lienzo gris.\n\nMis traumas,\nexplanadas de negro;\nconstantemente sueño\ncon el vacío de la noche.\n\nPesadillas recurrentes,\nen micro sueños\nque parecen eternos.\n\nLibido ahogada\npor parálisis de sueño.\n\nSin placer en lo banal,\nse deprimen los sentidos;\natrofiados,\nya no perciben\nlas cosas bellas de la vida.\n\nInsensible a los matices,\nsolo descanso\nentre ruido blanco.\n\nSolo la música\ntrae color\na mis recuerdos.\n\nY solo tú\ntraes\nel verde y rojo\nque necesito\npara no estar triste.",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 20,
        "name": "un_mundo_triste",
        "title": "Un Mundo Triste",
        "dedication": None,
        "body": "Un mundo triste\ndonde la gente aprende,\ndonde la gente crece.\n\nLlegan al límite\nde sus capacidades,\na la cúspide\ndel conocimiento.\n\nAgobiados por\nlas preguntas\nde antaño\nencuentran las\nrespuestas de siempre:\n\nQue no hay destino;\nque todo es azar.\n\nQue cualquier cosa es correcta\nsi se puede justificar.\n\nY aunque todo es relativo\ny nada sea verdad,\n\nel propósito de la vida\nsigue siendo\nla muerte.\n\nSolo con certeza de ello,\nviviendo en un mundo así,\n¿para qué prolongar\nlo inexorable?",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 21,
        "name": "acrilico",
        "title": "Acrílico",
        "dedication": None,
        "body": "Soñé con el abismo,\notra vez.\nCada vez más oscuro\ny cerca de mí.\n\nAl borde de la cornisa\ndescendiendo en\nen espiral,\ny cada noche,\nantes de despertar,\nme detengo\ny observo el cielo,\n\nOpaco y gris,\ncomo con un amanecer distante;\napagado y sordo,\nlloviendo siempre aquí.\n\nSoñé con el abismo,\notra vez.\nCada vez más oscuro\ny cerca de mí.",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 22,
        "name": "cliche",
        "title": "Cliché",
        "dedication": None,
        "body": "Impostora,\naunque seas plástica\neres la flor\nque más atrae\nzánganos.",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 23,
        "name": "cliche_ii",
        "title": "Cliché II",
        "dedication": None,
        "body": "¿Mångata?\nNo más que\nel reflejo tenue\nsobre charcos\nagonizantes.\n\nSe secan bajo el sol\ny desaparece la evidencia\nde tu brillo nocturno.\n\n¿Mångata,\ncómo que inmortal?\nSi dependes\nde lo efímero\npara ser visible.",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 24,
        "name": "dientes",
        "title": "Dientes",
        "dedication": None,
        "body": "Me quise despedir\ncon una carta origami.\nNo la hice,\nlos tiempos no me dieron;\ndices que no sé medirlos,\nque no sé medirme.\n\nTe iba a hacer un girasol,\no un gladiolo;\nverde, blanco y rojo.\n—Recuerdo lo que me dices\naunque acuses a mi memoria\nde ser peor que la tuya—.\n\nDentro iba a escribir\nque no buscaba simplemente\nuna amistad “literaria”.\nQue quería más\nazoteas,\nmás asientos traseros,\nmás rincones de cocina,\nbesos sobre vidrios,\ncicatrices y poemas.\n\nLo iba a escribir,\npero hoy\nte acompañé en el bus,\ny me mordiste,\nno lo esperaba.\nMe arrepentí.\nTus dientes me convencieron\nque no es necesario\npresionarte\npara encontrar en ti\nuna musa.",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 25,
        "name": "monotonia",
        "title": "Monotonía",
        "dedication": None,
        "body": "¿Cómo sigue todo con él?\nNo quieres hablar de eso, es complicado.\nEntiendo, entiendo.\n\nNo quiero incomodarte\nni ponerte a pensar\nen cosas poco placenteras.\n\nSolo quería saber de ti\nporque ayer\nme dijiste que\nes difícil no caer en la monotonía.\n\nHablaste de su amor,\nsobre cómo ha “madurado”;\nlo “estable” que es.\n\nEufemismos\npara maquillar el rescoldo\nde una pasión\nque ahogó su llama.\n\nLo sé,\nquieres volver a sentirlo:\nel calor del fuego\nantes de que queme.\n\nPero tienes miedo\nde acercarte tanto que\nno puedas apagarme\ncon un soplido.\n\nPero tranquila,\nmis intenciones no son\nmanipularte para que lo botes;\nsolo quiero que no dejes de ser\nmi musa.",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 26,
        "name": "stitch",
        "title": "Stitch",
        "dedication": None,
        "body": "Hola,\n¿cómo vas?\nTal vez te alegre saber\nque he vuelto a escribir.\n¿Y tú, qué has hecho con tu vida?\n\nEspero no haberte dañado la mente\ncon eso de reflexionar\nsobre ella,\n\npues yo\nhe estado sintiendo ansias\nal ver el cielo;\nme resulta difícil creer\nque pueda disipar la inconformidad\nque algunos sienten\npor la vida que no escogieron vivir.\n\n¿Quién la habrá escogido para mí?\n\nNo importa,\nsi es que al final\nmi ansiedad no viene de ahí.",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 27,
        "name": "cansancio",
        "title": "Cansancio",
        "dedication": None,
        "body": "Un ojo entreabierto\ny otro desconectado de la mente.\n\nA los de color negro\nse les ha privado\nla riqueza\nde una vida cromática.\n\nReloj de pulsera\nde cuero sadomasoquista.\n\nEl paso del tiempo\nes la herramienta de placer\npara quien disfruta\ndel sufrimiento de lo efímero.\n\nLágrimas erosionando\nla piel porosa entre tabique y pómulos.\n\nUn rostro tan golpeado\npor las gentiles\ngotas de rocío\nque traen las madrugadas.\n\nMadrugadas que espero despierto\nporque en mí no hay deseo de descansar.\n\nTu bofetada de realidad\nfue tan dura\nque mi imaginación ya ni se atreve\na soñar que soy tu dueño.\n\nSi no puedo soñarme\nsiendo feliz,\n¿qué sentido tiene dormir?",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 28,
        "name": "otra_forma_de_dolor",
        "title": "Otra Forma de Dolor",
        "dedication": None,
        "body": "La insensibilidad\nque trae el dolor\nno te vuelve\ninmune a la tristeza,\n\nporque el verdadero\nsufrimiento viene\nde la mente\n\n¿No me crees?\n\nCuando se cruza el umbral\nde dolor\nlos cuerpos\nceden a la insensibilidad.\n\nEmbriagado de adrenalina,\npodría tener\nlas tripas colgando\nen la acera\nsin sentir dolor\n\nTe lo digo,\nDios no fue\ntan cruel al crear al ser\nhumano después de todo.\n\n¿Pero, qué\nhizo el hombre?\n\nAlimentó su mente\ncon el fruto del\nárbol del conocimiento.\n\nY ahora\nconsciente,\nviendo tripas escurriéndose\npor la alcantarilla;\n\ngritos, llanto\ny maldiciones\n¿de dónde sale este dolor?\n\nYa te lo he dicho:\n\n“la ignorancia te…”\n\n¿Que por qué te digo esto?\n\nPara explicarte,\n\nque a pesar\nde que tu comentario\nno me haga sentir mal,\nsoy lo suficientemente inteligente\npara saber que\ndebería.\n\nY eso\nme pone triste.",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 29,
        "name": "caribe",
        "title": "Caribe",
        "dedication": None,
        "body": "Promuevo la idea\nde una obra opaca\ny visceral\nque cualquiera\nsea capaz de relacionar con\nla belleza\nque nace del dolor.\n\nPero la gente\nno quiere esforzarse\nen apreciar detalles,\n\nme tildan de hereje\ncuando trato de ejercitar\nsus mentes.\n\nPero el tiempo me dará la razón\nporque, aunque no sea santo,\nhablo con profecías:\n\npues “toda vida\nculmina en la muerte”\n\ny aunque no sepa si\nte gusta lo que escribo\nestoy seguro\nque algún día\nmorirás,\n\npero\n“nadie es profeta en su propia tierra”\n\ny\nmis palabras\nse disuelven en la humedad del aire.\n\nCálido, el Caribe\noprime el arte.\n\nSu sol\ntan agobiante,\n\nque con cariño remanente\nde noche\nacaricia al indigente\ny a mí\nno me deja dormir,\n\ndespierta a las nubes\nque emergen del mar.\nBailando,\nimitan el vaivén\nde las olas\ne inspiran\na la brisa\na cargar melodías cromáticas\nque no me dejan deprimir.\n\nImpone el buen clima\nsu alegría\nsobre los que queremos ver\nla vida color gris;\n\nsu calidez impide\nla creación\nde arte\nque no sea feliz.\n\nCon optimismo\nllena de brillo\nun lienzo opaco.\n\nYo mismo\nhe cometido este pecado,\n\npues\nhe notado que\naunque el cielo se oscurezca\nsolo con escuchar\nel grito de\nuna negra\nme pongo feliz.",
        "cover_url": libro_i_cover,
        "pages": 3,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 30,
        "name": "inspiracion",
        "title": "Inspiración",
        "dedication": None,
        "body": "La soledad.\nSentir que has vivido\ntoda la vida solo;\ntoda la vida sin amante.\n\nSaber que la muerte\nsepara la carne del deseo;\nencerrado en el cofre\nde un dios cambiante.\n\nEl olvido.\nInterpretar el recuerdo\ncomo único testigo\nde la realidad.\n\nSin memoria,\n¿cómo diferenciar\nlo que no se recuerda\nde lo que nunca ha existido?\n\nLo inevitable.\nLa dicotomía de la vida,\nsu propósito\nen la muerte.\n\nInfructuoso buscar\ninmortalidad en el arte,\nsi ni un dios sigue eterno\ncuando se abandona su culto.\n\nLa nada.\nSentir que has malgastado\nel significado\nque tú mismo has creado.\n\nSaber que has vivido sin amigos,\nfamilia, dios\nni amante.\n\nLa soledad.\nLa única\nque acompaña al escritor\ncuando observa en silencio,\napartado.",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 31,
        "name": "marea_baja",
        "title": "Marea Baja",
        "dedication": None,
        "body": "Criaturas marinas,\nnocturnas y abisales.\n\nA flote,\npesadillas existenciales.\n¿Qué son ellas\ny por qué se alimentan de mí?\n¿Qué es el mar,\ny cómo cabe tanto\nen mis sueños?\n\nCriaturas marinas,\nnocturnas y sin alma.\n\nA flote,\ntraumas de la infancia,\nser la suma\nde sobras de personalidad.\nLos demás\nconstruyen su inmortalidad\nsobre el recuerdo ajeno.\n\nCriaturas marinas,\nnocturnas y divinas.\n\nA flote,\npensamientos:\n¿Cuándo sueño soy un dios?\n— Y cuando despierto —\n¿Dios estará soñando?\n¿Qué le causa pesadillas a Dios,\nlos humanos?\n\nCriaturas marinas,\nnocturnas y sensibles.\n\nA flote,\n“nuevas ideas”,\nreciclaje de arquetipos.\nLa originalidad es autoengaño;\nla creatividad,\nla descripción\nde lo que ya todos hemos sentido\ncon palabras que a nadie\nse le han ocurrido.\n\nCriaturas marinas,\nnocturnas e invisibles.\n\nNadan en mis sueños,\nvagan en mis pensamientos;\nahí se nutren,\ny empiezan a crecer.\nTú no las ves,\ntú no las oyes,\npero ahí están,\nocultas bajo mi piel.\n\nCriaturas que\nhablan, nadan\ny observan.\n\nHablan, vagan\ny ríen.\n\nHablan, nadan\ny se alimentan de mí.",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 32,
        "name": "la_casa_de_las_goteras",
        "title": "La Casa de las Goteras",
        "dedication": None,
        "body": "Goteras sobre masas de periódico y tela;\nhace días empezó a apestar.\n\nEl hedor es denso y distrae,\ncomo testigo del tiempo\nque no se detiene.\n\nLa humedad se eleva\ny se escurre entre grietas,\npor las paredes hasta el techo;\n\ncomo profetizando\nque, desde los cimientos,\ntodo se desmoronará.\n\nEn cama,\nparece que fuera así.\n\nAtento\nobservo el techo,\nesperando que escombros\ncaigan sobre mí.\n\nHe somatizado la carga anímica,\neso tumor blanco y baboso\nno para de crecer.\n\nSe acomoda en mis cuencas\ny no me deja ver.\n\nY como mi paz mental\ndepende de mi lucidez,\nno tener claridad\n\nme hace sentir denso y pesado,\ndifícil de maniobrar.\n\nCegado,\natraigo pensamientos cubiertos\npor neblina gris,\ny ruido blanco.\n\nComo un mar de gente\nhasta el techo,\nsusurrando\ntodos al mismo tiempo.\n\nSin saber\nquién dice qué;\n\nsin escuchar\nuna voz conocida,\nsin ver\nun rostro familiar.\n\nEs el universo\nqueriendo colapsar\ndentro de mi pecho.\n\nEs todo\nprecipitado hacia un punto pequeño;\nun golpe seco,\nuna implosión gradual\n\nMi gravedad atrapando masa\ny dilatando el tiempo,\n\nsin abstracción, ni emociones.\nPura materia fugaz.\n\nSon mis propios pensamientos\narremetiendo contra mí\n\nFinalmente,\nla luz se extingue y\nlas estrellas se despiden del atardecer…\n\nMe detengo,\nalgo golpea mi cara.\nNo sé si cemento o agua.",
        "cover_url": libro_i_cover,
        "pages": 3,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 33,
        "name": "femme_fatale",
        "title": "Femme Fatale",
        "dedication": None,
        "body": "Una amante,\nuna musa\nun sol, una estrella.\n\nLa inspiración disruptiva\nque alimenta el poema.",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 34,
        "name": "die_rosenrot",
        "title": "Die Rosenrot",
        "dedication": None,
        "body": "Ya habías abierto tus pétalos\ny andabas despreocupada,\nregándolos por ahí;\ndía y noche\nbailabas,\nacaparando miradas\ny enamorando al sol.\n\nRosa roja\ncomo sangre\nsadomasoquista,\ncolor intenso e indecente\ncomo el deseo de poseerte,\nde clavarme tus espinas,\ncada una de ellas\nsolo por el placer\nde volver a sentir.\n\nClavar unas en mi lengua\npara no halagar\notra flor.\n\nOtras en mi cuello,\ncomo penitente por el arte.\n\nY solo una en mi mente,\nsuficiente para no olvidar\nque idealizaba una vida\njunto a ti.\n\nLastimosamente, rosa,\nya no eres roja,\nno como recordaba.\n\nHas rapado cada pétalo\ny ya solo\nquedan espinas.\n\nTe has marchitado,\ny no parece\nque te vayas a detener.\n\nAun así,\nsería un privilegio\nverte morir,\n\nporque vives orgánica.\nNo eres plástica\ncomo aquellas\nque buscan acaparar el sol.\n\nPor eso,\nme gustaría\npresenciar tu muerte,\n\no la nuestra.\n\nSi lo permites,\ncon gusto te apretaría con suficiente fuerza\npara desangrar mi pecho sobre ti.\n\nSer mártir,\nsolo para que vivas\nlo que te queda\ncomo la rosa más roja.",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 35,
        "name": "reflexion_x",
        "title": "Reflexión X",
        "dedication": None,
        "body": "¿Y si\nnuestra conciencia\nes el recuerdo\nde un yo\nagonizando\nen el presente?",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

content_poemas_para_mi = [
    {
        "poem_id": 36,
        "name": "entre_dientes",
        "title": "Entre Dientes",
        "dedication": None,
        "body": "Evasivamente\nte respondo:\n«no tengo nada».\n¿No lo entiendes?\nSí “tengo algo”:\nme desmorono por dentro.\n\nTe digo:\n«no pasa nada».\n¿Qué no ha pasado?\n¿Acaso no lo ves?\nSiento que\nno puede ocurrir\nnada peor.\n\nTe evito con un\n«solo estoy cansado».\n¡Despierta!\nA gritos te dejo saber\nque estoy aburrido\nde lo cotidiano.\n\nTe explico\n«El nihilismo “esto” …\nNihilismo “aquello”».\nTe estoy diciendo\n—no en broma—\nque no le encuentro\nsentido a la vida.\n\nTe comparto\notro de mis pensamientos:\n\n“Ansío la muerte”,\naunque nunca lo escuches,\nlo grito entre dientes.",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 37,
        "name": "lounova",
        "title": "Lounová",
        "dedication": None,
        "body": "Solía preguntarte:\n¿por qué eres tan perfecta?\nAhora pienso:\n¿por qué me gustas tanto?\n\nQuisiera saberlo,\nen serio,\npara que dejara de ser así;\nporque\n«la ignorancia te hace feliz»\ny el conocimiento de tu ausencia\nme desgarra las entrañas,\nel espíritu,\nla mente\ny el alma.\n\nCada mensaje tuyo\nes una pequeña dosis\nque aumenta mi dependencia a ti;\nadicto a una ilusión,\nadicto a tu recuerdo.\n\nAdicción\nque calmo\ncon autoengaño:\nla única opción, real,\nque siempre ha estado ahí.\n\nPero no es sano\neludir la realidad\npara fantasear contigo.\n\nDebo aceptar que fuiste\nun dulce sueño\nque se olvida al despertar.\n\nSolo me queda,\nen contra de cada impulso,\nconvencerme de que\nya no eres mi musa,\nque quizá\nnunca lo fuiste,\ny despedirme.\n\nUn adiós\nnunca sonó tan agrio.",
        "cover_url": poemas_para_mi_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 38,
        "name": "novia",
        "title": "Novia",
        "dedication": None,
        "body": "De madrugada\nel insomnio induce un transitorio en mí.\nHace dos segundos,\napoyado en tus caderas,\nbuscaba constelaciones en tus pecas;\nun segundo después,\ndesperté.\n\nLa realidad me susurró.\n—No hay caderas, no hay pecas.\nNo hay pelo, ojos ni piel;\nrojo, verde ni blanco.\n\nY ahora,\npor la comisura de mi ojo,\nse fugan lágrimas.\nBoca arriba miro,\nmás allá del techo,\nhacia mi destino:\n\nLa soledad y la frustración.\n\nPorque cuando pude\nno era el tiempo de Dios.\nY hoy que quiero, sé\nque, a causa mía,\nno has sido, no eres\ny estoy convencido\nque tampoco serás.",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 39,
        "name": "zplplplyk",
        "title": "[ZPLPLPLYK]",
        "dedication": None,
        "body": "Mal viajado, mi mente es poseída\npor una macabra melodía infantil; arte puro y diabólico.\n¿El himno de mis traumas?\nReverbera en mi pecho, se sobrepone a sus palabras, a mis canciones.\nEs poderosa y no sé por qué. Trato de ignorarla\npero cada movimiento asemeja su forma.\nUn arquetipo, un concepto, un símbolo.\n¿Subliminal, ancestral?\nUn talismán rectangular grande y arqueado\ncon un cuadrado en su base.\n[ZPLPLPLYK], [ZPLPLPLYK].\nPalabras que no entiendo, palabras que\nno puedo pronunciar;\nun ritmo en 5/4\nen el que no logro encajar.\nGolpes de negras que me impactan\ndanzando en rituales de santería.\nLa Sardana de las Brujas,\ndescalzas sobre mi halo,\nlo ensucian, se pudre.\nMe dañan la mente para que las acepte,\nporque me han escogido\n«Santo»\nsegún su pagana providencia.\nBloquean mis plegarias,\nbloquean a Dios.\nRecobro la conciencia por intervalos cortos,\ncada vez más cerca del suelo.\nMe acuesto frente al sofá,\nme arrastro hacia el baño.\nRecobro la conciencia de mi frustración\ntirado besando el piso.\nRecobro el sentido del dolor\nvomitando sangre.\n¿Mala hierba o placebo?\nNo importa, somatizo el viaje.\n[ZPLPLPLYK], [ZPLPLPLYK].\nCantos chillones, sollozos graves,\ngemidos no temperados,\ncadenas que se arrastran.\nUn compás de amalgama\ncompuesto por amplios matices\nde emociones fuertes.\nLanzo la mirada al pasillo\nmientras me arrastro por el marco\ny llamo a Frank.\nUn grito que se ahoga buscándolo\nen la lejanía creciente.\nCuando logra verme,\nya en el infinito,\nNo puede contener la risa.\nMis gimoteos nunca llegaron a sus oídos,\nsolo la patética imagen\nde un pretencioso que se perdió\nen sus propios pensamientos.\nImagen que comparten las musas,\ntapan sus delicadas boquitas\npara ocultar risotadas depravadas.\nMorbosas observan\nel espectáculo más bochornoso:\nun «artista»\narrastrándose por el suelo,\ntodo por encontrar un poco de inspiración.\n¿Qué obtuve?\n[ZPLPLPLYK], [ZPLPLPLYK].\nArmonías, melodías,\nritmos que no entiendo…\nPalabras que no soy capaz de escribir,\nun mal viaje que no quiero repetir\ny el temor de que todo\nhaya sido producto\nde mi propia mente.",
        "cover_url": poemas_para_mi_cover,
        "pages": 3,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 40,
        "name": "miketta",
        "title": "Miketta",
        "dedication": None,
        "body": "Eres la primera artista\nque he acariciado\ncon indecencia,\nrasguños\nde mis manos “mágicas”\nde guitarrista\nfrustrado.\n\nY aunque\nsangraste,\nme impresionó\ntu nobleza:\nno sentiste dolor,\nsentiste vergüenza.\n\nVergüenza por dos dedos\nmanchados de sangre,\npor tu mordida\nen mi brazo.\nVergüenza\npor\nmostrar tus deseos\nde forma natural.\n\nVergüenza que veo\ny me hace sentir culpable.\n\nEres la inocencia\ny bondad\nque necesito\ncorromper.\n\nDeseo desatar los nudos\nque mantienen tu mente\natada a los clichés.\n\nPresentarte a mis musas:\nla realidad,\nel insomnio, la tristeza\ny la depresión.\n\nInvitarlas a que\ninspiren tus obras,\nnuestra futura\nhistoria:\nla única carta\nde desamor\nque me interesa leer.\n\nTe detallo\ncon detenimiento\npara comprender\nel porqué de\ntus lágrimas.\n\nTe detallo\ncon detenimiento\npara saber qué\nquieres escuchar.\n\nTe digo que soy\ntodo un caballero\nmientras metódicamente\npaseo mis yemas\nsobre tu lomo.\n\nMe di cuenta de cómo\nacariciar tu tatuaje;\ny tú,\nde que realmente\ntraigo intenciones\nde hacerte daño.",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 41,
        "name": "manipulacion",
        "title": "Manipulación",
        "dedication": None,
        "body": "Ayer te mordí un pezón\ny creo que envenené tu pecho.\n\nAparentemente fue profundo\ny llegó a tus pulmones,\nporque hoy andas\nrespirando con dificultad,\ncomo agonizando.\n\nMe detallas erráticamente\ncon una mirada\napagada,\nbuscándole explicaciones\na mi forma de actuar.\n\nLa esperanza de encontrar\nmi bondad.\n\nMe da lástima\nverte lamentar\nla inexorable insatisfacción\nde tu búsqueda.\n\nNo encontrarás nada bueno\nen mí,\nsolo diezmarás tu fe.\n\nPero te entiendo.\nDespués de todo,\ndel veneno\nse obtiene el antídoto.\n\n—Con nuevos traumas—.\n¿Qué vacío buscas llenar?",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 42,
        "name": "insuperable",
        "title": "Insuperable",
        "dedication": "Lounová",
        "body": "Increíble,\ncuatro años\ny sigues siendo\nun pensamiento recurrente.\n\nUn olor fugaz\nque guardo en mis pulmones.\n\nLa acidez constante\nque quema mi paladar.\n\nUna implosión incesante\nreverberando en mi pecho.\n\nEl vacío\nque no me siento listo para llenar.\n\nTrato de hacerlo\nreconstruyéndote con palabras,\npero inevitablemente\ncaigo en el suelo común,\nreventándome con fuerza\ncontra la realidad:\n\nQue tú no estás,\nque te necesito,\ny que, aunque eres la musa perfecta,\nno soy suficiente para ti.\n\nPorque no he logrado\ncombinar las palabras perfectas\npara inmortalizar tu belleza.\n\nPorque no he logrado\nbajarte del Parnaso\npara exhibirte ante los incrédulos\ne insensibles.\n\nTal vez,\npor eso no merezca tenerte;\no simplemente\nno me he esforzado\nlo suficiente.\n\nNo he consagrado mi vida\na inmortalizar la tuya,\nescribiendo el poema perfecto.\n\nNi han presionado mis dedos\ncon suficiente fuerza\nel teclado hasta sangrar.\n\nSi no he arriesgado mi vida\npara llegar a donde estás,\n\ncómo podría ser tan hipócrita\npara luego decirte\nque moriría por ti?",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 43,
        "name": "abuela",
        "title": "Abuela",
        "dedication": None,
        "body": "Me siento un poco hipócrita\nrecibiendo el\n“sentido pésame”.\n\nYo nunca fui apegado a ella\ny honestamente\nno me siento mal\npor su muerte.\n\nDe hecho, me siento tranquilo\nporque su agonía terminó.\n\nPor eso,\ndeberían acercarse con un\n“lamento que sufriera\nen sus últimos momentos”.\n\nEso sí es consuelo,\npodría creer que es\nun comentario sincero.\n\nPorque la empatía\nnace de entender el dolor ajeno,\n\ny aunque no la quise,\nsiento tristeza\nporque la vi sufrir.\n\nDesahuciada\ncon una lagrima\nnos dio a entender\nque sufrió al aceptar su muerte.\n\nAl menos en ella\nencontró liberación\ny ya no hay más sufrimiento,\n\no bueno\núnicamente queda\nel de los que vivos\nlloran su muerte.",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 44,
        "name": "balcon",
        "title": "Balcón",
        "dedication": None,
        "body": 'Si se te antoja saltar, llámame\ny nos tiramos los dos.\n\nAsí verás que no miento,\ncuando te digo:\n"el amor es una decisión";\n\nque, si me das tu mano,\nme aferraría a ella el resto de mi vida,\n\ny que aceptar la muerte,\nno es tan difícil,\nsi te tengo junto a mí.',
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 1,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

content_book_ii_eng = [
    {
        "poem_id": 1,
        "name": "god",
        "title": "God",
        "dedication": None,
        "body": "Don't heal me.\nI want sadness,\nI want depression;\nthey are my muses,\ndon't take them away.\nDo not fill me,\nI am so full,\nthat I don’t accept more.\nI feel nauseous\nwhen they talk to me about purposes.\nI would like to vomit,\nleave my mind blank,\nignore everything\nand —perhaps— be happy.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 2,
        "name": "identity",
        "title": "Identity",
        "dedication": None,
        "body": "Explore the storm.\nTouch yourself and feel\nhow everything is\nwind, sand, and dirt;\none dry season,\nanother one, wet.\nYou are a pendulum\nthat swings\nbetween tears and anger;\nsometimes ascetic,\nsometimes a sinner.\nFrom warm to cold,\nyou stir yourself.\nNever constant,\neach time heavier\nit’s hard for you to oscillate.\nWhat are you?\nNot the you;\nbut the infinite sum\nof what surrounds you:\nfinite impulses,\nalien wills.\nWhen you stop,\nin balance,\nyou will realize.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 3,
        "name": "spica",
        "title": "Spica",
        "dedication": None,
        "body": "You,\nartist and muse,\nan impossible dichotomy.\nBetween your worship and the celestial,\nI prefer condemnation.\nMartyr for you,\nwhom veiled\nbetween heaven and earth,\nwelcomes under your shadow\nthe nonconformists.\nFor the weary\nof dawn and dusk,\nyou are the salvation of the everyday,\nour eternal eclipse.",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 4,
        "name": "moral",
        "title": "Morality",
        "dedication": None,
        "body": """It can always get worse,
fall deeper.
The light at the end of the tunnel is left behind,
and you wonder:
Will I ever hit bottom?
You fall for so long
that up or down
makes no sense;
better or worse makes no difference.
You think:
What should I do?
—Don’t do.
Be, exist.
Enjoy your wickedness, your goodness,
whatever you are;
however it is,
soon
you will collide with the abyss.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 5,
        "name": "exhortation",
        "title": "Exhortation",
        "dedication": None,
        "body": """Love, disaster.
Among all the deserts,
the cactus pricks at the sun,
bleeds and scorches the earth.
The Sphinx’s sandals
do not shield her from the flames.
Abandoned
—poetry and music—
buried among the dunes.
Those who managed to escape
were caught by the shadow.
Thousands of notes, rhythms, and chords
extinguished by a sandstorm,
like a rain of bullets,
an artistic genocide.
Everyone is given a life,
but who can become immortal.
Write, carve, scream, record.
Artist, your days are numbered.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 6,
        "name": "writers_voice",
        "title": "Writer's Voice",
        "dedication": None,
        "body": """I found my writer’s voice.
It’s guttural,
—muted and raspy—
filled with pessimism.

It proclaims:
—Ignorance makes you happy.

That’s why
when I call you,
ignore me
and look
towards where white noise
obscures my voice.

Every time I invite you,
with a defeated look,
to reflect
on life,
cover your eyes
and move away from me.

But, why?
You keep reading.

Follow my voice,
I will free you from happiness.

From a corner,
I call you to the shade
where everything is knowledge.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 7,
        "name": "defeatism",
        "title": "Defeatism",
        "dedication": None,
        "body": """Life begins halfway
when you decide between
being the ripest fruit in the treetop
or going back and not sprouting.
I chose to go back, not to be it;
to descend in the hierarchy.
To warn, convince others
of the imminent trap:
up there, only waiting to be devoured
or ignored;
eventually fall and rot.
Two paths that lead
to the same dung pit
to nourish the cycle again.
I didn’t want more effort in vain
so I found the roots,
at the deepest.
Finished, I drowned in the earth
and had no more pretensions
to see the sun again.
I flooded that dry and weary tree with tears.
I discovered that
the penances borne by knowledge
are loneliness and sadness,
failure.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 8,
        "name": "rat_utopia",
        "title": "Rat Utopia",
        "dedication": None,
        "body": """At the pinnacle of development,
plastic hands mold morality:
The masculine
is forced into the feminine,
which in turn
marches to its encounter;
in the center, they merge
and bewildered,
they themselves
are no more.
Alienated, they want to cry,
they cannot;
there are no emotions,
only automatons
reacting to stimuli.
Love, hatred;
ambitions, humanity:
social constructions,
defects of the system.
Power defeats competition
and corrupt hierarchies
come crashing down.
Blame is cast left, right;
on the Devil, on God.
They became indifferent long ago.
On the other hand,
Bacchus gets drunk
and enjoys the panorama:

Post-apocalyptic, postmodern;
without roles, without identity.
The coveted anarchy:
A rat utopia.""",
        "cover_url": libro_ii_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 9,
        "name": "reflection_ii",
        "title": "Reflection II",
        "dedication": None,
        "body": """To elude the inevitable
is to speak of God.
Speaking of God is
to think outside of time.
Thinking outside of time
is to dream.
Dreaming is to fantasize
that life’s problems
vanish in the act of writing.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 10,
        "name": "reflection_iii",
        "title": "Reflection III",
        "dedication": None,
        "body": """The artist is not in the work,
the artist is in the soul:
between the mind and the heart,
through the lungs,
beneath the sternum;
where the cigar,
after each draw,
leaves a glowing ember.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 11,
        "name": "reflection_iv",
        "title": "Reflection IV",
        "dedication": None,
        "body": """At night
on the beach,
the smoke dissipates
in a magical way;
it takes on a different demeanor,
trying to mimic the serenity of the sea.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 12,
        "name": "reflection_xii",
        "title": "Reflection XII",
        "dedication": None,
        "body": """I oscillate between the bad and the worse;
not being the best version of myself,
and not wanting to be.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 13,
        "name": "its_not_enough",
        "title": "It's not enough",
        "dedication": None,
        "body": """It’s curious
that not being the best
version of yourself
makes you bad.

And not wanting to be
makes you worse.

The perplexing thing
is that
to be good
it’s not enough to just want to be.""",
        "cover_url": libro_ii_cover,
        "ig_url": """""",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 14,
        "name": "czech",
        "title": "Czech",
        "dedication": None,
        "body": """The first step
to overcome an addiction
is to accept it.

You can’t mask
drunkenness
believing you are sober.

To move over you,
I must accept
that there are parts of you
I can’t forget.

And it’s not an obsession with you,
but with what you represent:
The idealization of a woman;
the perfect muse.

The eternal whim
of wanting
what I cannot attain.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 15,
        "name": "hatred",
        "title": "Hatred",
        "dedication": None,
        "body": """I will shave my eyebrows
and tear my garments;
turned into a complete ascetic,
hermetic,
I will close the valve of my soul.
No more s of emotions;
stagnant,
they will turn me into carrion.
Mangy and stray,
I will howl at the moon
and without decorum, I will show indulgence
for my own weakness.

There is no mercy
in wisdom.
There is no wisdom
in weariness;
so bored of the common,
so tired of failure.

Without stories,
mine are recurring words,
vaguely connected phrases;
intense colors
that abstract everything to figures,
the search for meaning
leading me to nothing,
forcing a thought
vulgarizing intellect;
the hatred for myself.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 16,
        "name": "she",
        "title": "She",
        "dedication": None,
        "body": """You loved her, in your way.
Under an uneven yoke,
you broke her neck.
And with oaths,
you promised change,
but not from your end.
You deceived her,
and her blind faith exacerbated her alienation.
From artist to muse,
her gaze changed:
her radiance, her eyes.
She became your model.
Transfigured,
you consecrated her to your altar
alongside the Pleiades
where she now rests,
stripped of her body;
which, buried by time,
without a cross or epitaph,
was forgotten.
Will she rest in peace?
Who was she?
The girlfriend of...""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 17,
        "name": "half_red_lucky_pack",
        "title": "Half Red Lucky Pack",
        "dedication": "Mångata",
        "body": """One cig.
We talked about love and the soul.
We don’t know them, who does?
Yet, she spoke of her ex,
and I of the one I’ve never had.

Two cigs.
We talked about otherness:
everyone knows each other,
but no one understands anyone.
—We will never truly be friends.
—I don’t pretend we will.

Three cigs.
Resorted to blows,
ignored words.
Fists that speak
of long-standing resentments.
I just observe.

Four cigs.
Words through smoke.
We kill time,
we burn tobacco.
We look at each other, we laugh;
we gaze at the sky,
we exhale.

Five cigs.
—The last one is sacred.

Silence,
a symbol of our friendship.""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 18,
        "name": "reflection_ix",
        "title": "Reflection IX",
        "dedication": "my faith",
        "body": """“The devil knows more
by being old
than by being a devil.”
If the wisdom
that only eons
can bring
has not moved him toward a change,
why should I
seek virtue
in holiness?""",
        "cover_url": libro_ii_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

content_book_i_eng = [
    {
        "poem_id": 19,
        "name": "nostalgia",
        "title": "Nostalgia",
        "dedication": None,
        "body": """I Remember. . .
the good times past
like opaque brushstrokes
on a gray canvas.

My traumas,
esplanades of black;
constantly, I dream
of the emptiness of the night.

Recurring nightmares,
in micro-dreams
that seem eternal.

Libido drowned
by sleep paralysis.

Without pleasure in the mundane,
the senses become depressed;
atrophied,
they no longer perceive
the beautiful things in life.

Insensitive to nuances,
I only rest
within white noise.

Only music
brings color
to my memories.

And only you
bring
the green and red
I need
to not be sad.""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 20,
        "name": "a_sad_world",
        "title": "A Sad World",
        "dedication": None,
        "body": """A sad world
where people learn,
where people grow.

They arrive at the limit
of their capabilities,
at the pinnacle
of knowledge.

Overwhelmed by
the questions
of yesteryear,
they find the
same old answers:

That there is no destiny;
that everything is chance.

That anything is right
if it can be justified.

And though everything is relative
and nothing is true,

the purpose of life
is still
death.

Only certain of this,
living in such a world,
why prolong
the inexorable?""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 21,
        "name": "acrylic",
        "title": "Acrylic",
        "dedication": None,
        "body": """I dreamed of the abyss,
once again.

Each time darker
and closer to me.

On the edge of the ledge
descending in
a spiral,

and every night,
before waking up,
I stop
and observe the sky,

Opaque and gray,
as if with a distant dawn;

dim and muted,
always raining here.

I dreamed of the abyss,
once again.

Each time deeper
and within me.""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 22,
        "name": "cliche",
        "title": "Cliché",
        "dedication": None,
        "body": """Imposter,
even if you’re plastic,
you are the flower
that most attracts
drones.""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 23,
        "name": "cliche_ii",
        "title": "Cliché II",
        "dedication": None,
        "body": """Mångata?
Nothing more than
the faint reflection
on dying
puddles.

They dry under the sun
and the evidence
of your nocturnal glow disappears.

Mångata,
what do you mean inmortal?
When/if you depend
on the ephemeral
to be visible.""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 24,
        "name": "teeth",
        "title": "Teeth",
        "dedication": None,
        "body": """I wanted to say goodbye
with an origami letter.
I didn’t make it,
I didn’t have the time;
you say I don’t know how to measure it,
that I don’t know how to measure myself.

I was going to make you a sunflower,
or a gladiolus;
green, white, and red.
—I remember what you tell me
even if you accuse my memory
of being worse than yours—.

Inside, I was going to write
that I wasn’t just looking for
a "literary" friendship.
That I wanted more
rooftops,
more back seats,
more kitchen nooks,
kisses on glass,
scars and poems.

I was going to write it,
but today
I accompanied you on the bus,
and you bit me,
I didn’t expect it.
I regretted it.
Your teeth convinced me.

that it is not necessary
to press you
to find a muse in you.""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 25,
        "name": "monotony",
        "title": "Monotony",
        "dedication": None,
        "body": """How is everything with him?
You don’t want to talk about it, it’s complicated.
I understand, I understand.

I don’t want to make you uncomfortable
or make you think
unpleasant things.

I just wanted to know about you
because yesterday
you told me
it’s difficult not to fall into monotony.

You talked about his love,
about how he has "matured";
how "stable" it is.

Euphemisms
to disguise the embers
of a passion
that stifled its flame.

I know,
you want to feel it again:
the warmth of fire
before it burns.

But you’re afraid
to get so close that
you can’t extinguish me
with a blow.

But don’t worry,
my intentions are not
to manipulate you to cast him aside;
I just don’t want you to stop being
my muse.""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 26,
        "name": "stitch",
        "title": "Stitch",
        "dedication": None,
        "body": """Hello,
how are you?
Perhaps it will please you to know
that I’m back to writing.
And you, what have you done with your life?

I hope I haven’t harmed your mind
with that business of reflecting
on it,

because I
have been feeling anxious
when looking at the sky;
it’s hard for me to believe
it can dispel the dissatisfaction
that some feel
for the life they didn’t choose to live.

Who might have chosen it for me?

It doesn’t matter,
if, in the end,
my anxiety doesn’t come from there.""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 27,
        "name": "weariness",
        "title": "Weariness",
        "dedication": None,
        "body": """One eye half-open
and the other disconnected from the mind.

Those of black color
have been deprived
the richness
of a chromatic life.

Wristwatch
of sadomasochistic leather.

The passage of time
is the tool of pleasure
for those who enjoy
the suffering of the ephemeral.

Tears eroding
the porous skin between septum and cheekbones.

A face so battered
by the gentle
drops of dew
brought by the early mornings.

Early mornings I await awake
because in me there is no desire to rest.

Your slap of reality
was so harsh
that my imagination no longer dares
to dream that I am your owner.

If I cannot dream
of being happy,
what’s the point of sleeping?""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 28,
        "name": "another_form_of_pain",
        "title": "Another Form of Pain",
        "dedication": None,
        "body": """The insensitivity
that pain brings
does not make you
immune to sadness,

because true
suffering comes
from the mind.

Don’t you believe me?

When the threshold
of pain is crossed,
bodies
yield to insensitivity.

Drunk on adrenaline,
I could have
my guts hanging
on the sidewalk
without feeling pain.

I tell you,
God was not
so cruel when creating
the human being after all.

But what
did man do?

He fed his mind
with the fruit of
the tree of knowledge.

And now
conscious,
seeing guts oozing
through the sewer;

cries, weeping,
and curses
where does this pain come from?

I’ve already told you:

"ignorance makes..."

Why do I tell you this?

To explain to you,

that despite
your comment
not hurting me,
I am intelligent enough
to know that
it should.

And that
makes me sad""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 29,
        "name": "caribbean",
        "title": "Caribbean",
        "dedication": None,
        "body": """I promote the idea
of an opaque
and visceral work
that anyone
can relate to
the beauty
that is born from pain.

But people
don’t want to make the effort
to appreciate details;

they label me a heretic
when I try to exercise
their minds.

But time will prove me right
because, although I am no saint,
I speak with prophecies:

for "every life
culminates in death."

And though I may not know
if you like what I write,
I am sure
that someday
you will die,

but
"no one is a prophet in their own land."

And
my words
dissolve in the humidity of the air.

Warm, the Caribbean
oppresses art.

Its sun
so overwhelming,

that with lingering affection
at night
caresses the homeless
and to me
it doesn’t let me sleep,

awakens the clouds
that emerge from the sea.

Dancing,
they mimic the sway
of the waves
and inspire
the breeze
to carry chromatic melodies
that won’t let me get depressed.

The good weather imposes
its joy
on those of us who want to see
life in shades of gray;

its warmth prevents
the creation
of art
that is not happy.

With optimism
fills with brightness
a dull canvas.

I myself
have committed this sin,

for
I have noticed that
even if the sky darkens,
just by hearing
the cry of
a black woman,
I become happy.""",
        "cover_url": libro_i_cover,
        "pages": 3,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 30,
        "name": "inspiration",
        "title": "Inspiration",
        "dedication": None,
        "body": """Loneliness.
Feeling that you have lived
your whole life alone;
your whole life without a lover.

To know death
separates flesh from desire;
confined in the chest
of a changing god.

Oblivion.
Interpreting memory
as the sole witness
of reality.

Without memory,
how to distinguish
what is not remembered
from what has never existed?

The inevitable.
The dichotomy of life,
its purpose
in death.

Fruitless to seek
immortality in art,
if not even a god remains eternal
when its worship is abandoned.

The nothingness.
Feeling that you have squandered
the meaning
that you yourself have created.

Knowing that you have lived without friends,
family, god,
or lover.

Loneliness.
The only one
that accompanies the writer
when observing in silence,
secluded.""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 31,
        "name": "low_tide",
        "title": "Low Tide",
        "dedication": None,
        "body": """Marine creatures,
nocturnal and abyssal.

Afloat,
existential nightmares.
What are they
and why do they feed on me?
What is the sea,
and how does so much fit
in my dreams?

Marine creatures,
nocturnal and soulless.

Afloat,
childhood traumas,
being the sum
of personality leftovers.
Others
build their immortality
on other poeple’s memories.

Marine creatures,
nocturnal and divine.

Afloat,
thoughts:
When I dream, am I a god?
— And when I wake up —
Is God dreaming?
What causes God nightmares,
humans?

Marine creatures,
nocturnal and sensitive.

Afloat,
"new ideas",
recycling of archetypes.
Originality is self-deception;
creativity,
the description
of what we have all already felt
with words that no one
has thought of.

Marine creatures,
nocturnal and invisible.

They swim in my dreams,
wander in my thoughts;
there they nourish,
and they begin to grow.
You don’t see them,
you don’t hear them,
but there they are,
hidden beneath my skin.

Creatures that
speak, swim
and observe.

Speak, wander
and laugh.

Speak, swim
and feed on me.""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 32,
        "name": "the_house_of_leaks",
        "title": "The House of Leaks",
        "dedication": None,
        "body": """Leaks over masses of newspaper and cloth;
it started to stink days ago.

The stench is dense and distracting,
as a witness of time
that does not stop.

Humidity rises
and seeps through cracks,
through the walls to the ceiling;

as if prophesying
that, from the foundations,
everything will crumble.

In bed,
it seems as if it were so.

Attentive,
I observe the ceiling,
waiting for debris
to fall upon me.

I have somatized the emotional burden,
that white and slimy tumor
keeps on growing.

It settles in my eye sockets
and doesn’t let me see.

And as my mental peace
depends on my lucidity,
not having clarity
makes me feel dense and heavy,
difficult to maneuver.

Blinded,
I attract thoughts covered
by gray mist,
and white noise.

Like a sea of people
up to the ceiling,
whispering
all at the same time.

Without knowing
who says what;
without hearing
a familiar voice,
without seeing
a familiar face.

It’s the universe
trying to collapse
inside my chest.

It’s everything
precipitated towards a small point;
a sharp blow,
a gradual implosion.

My gravity trapping mass
and dilating time,
without abstraction, nor emotions.
Pure fleeting matter.

It’s my own thoughts
lashing out against me.

Finally,
the light extinguishes and
the stars bid farewell to the sunset...

I pause,
something hits my face.
I don’t know if it’s cement or water.""",
        "cover_url": libro_i_cover,
        "pages": 3,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 33,
        "name": "femme_fatale",
        "title": "Femme Fatale",
        "dedication": None,
        "body": """A lover,
a muse
a sun, a star.

The disruptive inspiration
that feeds the poem.""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 34,
        "name": "the_red_rose",
        "title": "The Red rose",
        "dedication": None,
        "body": """You had already opened your petals
and wandered carefree,
scattering them around;
day and night
you danced,
capturing glances
and making the sun fall in love.

Red rose
like sadomasochistic
blood,
intense and indecent color
like the desire to possess you,
to pierce me with your thorns,
each one of them
just for the pleasure
of feeling again.

To pierce some into my tongue
so as not to praise
another flower.

Others into my neck,
as a penitent for art.

And only one in my mind,
enough not to forget
that I idealized a life
together with you.

Unfortunately, rose,
you are no longer red.
Not as I remembered.

You have shaved every petal
and now only
thorns remain.

You have withered,
and it doesn’t seem
like you’re going to stop.

Even so,
it would be a privilege
to see you die,

because you live organically.
You are not plastic
like those
who seek to monopolize the sun.

That’s why,
I would like
to witness your death,

or ours.

If you allow it,
I would gladly squeeze you with enough force
to bleed my chest over you.

To be a martyr,
just so you can live
what remains for you
as the reddest rose.""",
        "cover_url": libro_i_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 35,
        "name": "reflection_x",
        "title": "Reflection X",
        "dedication": None,
        "body": """What if
our consciousness
is the memory
of a self
agonizing
in the present?""",
        "cover_url": libro_i_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

content_poemas_para_mi_eng = [
    {
        "poem_id": 36,
        "name": "between_teeth",
        "title": "Between Teeth",
        "dedication": None,
        "body": """Evasively
I answer you:
"I have nothing."
Don’t you understand?
I do "have something":
I crumble inside.

I tell you:
"Nothing happens."
What hasn’t happened?
Can’t you see it?
I feel that
nothing worse
can happen.

I avoid you with a
"I’m just tired."
Wake up!
With screams I let you know
that I am bored
of the everyday.

I explain to you
"Nihilism ’this’...
Nihilism ’that’."
I am telling you
—not joking—
that I don’t find
meaning in life.

I share with you
another of my thoughts:
"I long for death,"
even if you never hear it,
I shout it between teeth.""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 37,
        "name": "lounova",
        "title": "Lounová",
        "dedication": None,
        "body": """I used to ask you:
why are you so perfect?
Now I wonder:
why do I like you so much?

I’d like to know,
seriously,
so that it would stop being like this;
because
"ignorance makes you happy"
and the knowledge of your absence
tears apart my insides,
my spirit,
my mind
and my soul.

Every message from you
is a small dose
that increases my dependence on you;
addicted to an illusion,
addicted to your memory.

Addiction
that I soothe
with self-deception:
the only real option,
that has always been there.

But it’s not healthy
to evade reality
to fantasize about you.

I must accept that you were
a sweet dream
forgotten upon waking.

All that’s left for me,
against every impulse,
is to convince myself that
you are no longer my muse,
that perhaps
you never were,
and say goodbye.

A farewell
never sounded so bitter.""",
        "cover_url": poemas_para_mi_cover,
        "pages": 2,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 38,
        "name": "girlfriend",
        "title": "Girlfriend",
        "dedication": None,
        "body": """In the early morning
insomnia induces a transient in me.
Two seconds ago,
leaning on your hips,
I searched for constellations in your freckles;
a second later,
I woke up.

Reality whispered to me.
—There are no hips, no freckles.
There is no hair, eyes, or skin;
red, green, or white.

And now,
from the corner of my eye,
tears leak.
Face up I look,
beyond the ceiling,
towards my destiny:

Loneliness and frustration.

Because when I could
it wasn’t God’s time.
And now that I want, I know
that, because of me,
you haven’t been, you aren’t
and I am convinced
that you won’t be either.""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 39,
        "name": "zplplplyk",
        "title": "[ZPLPLPLYK]",
        "dedication": None,
        "body": """Badly tripping,
my mind is possessed
by a macabre childish melody;
pure and diabolical art.
The anthem of my traumas?
It reverberates in my chest,
overpowers their words,
my songs.
It is powerful
and I don’t know why.
I try to ignore it
but every movement
resembles its form.
An archetype, a concept, a symbol.
Subliminal, ancestral?
A large, arched rectangular talisman
with a square at its base.
[ZPLPLPLYK], [ZPLPLPLYK].
Words I don’t understand,
words that
I can’t pronounce;
a 5/4 rhythm
in which I cannot fit.
Quarter-note beats strike me
dancing in rituals of Santeria.
The Sardana of the witches,
barefoot on my halo,
they soil it, let it decay.
They damage my mind so I accept them,
because they have chosen me
"Saint"
according to their pagan providence.
They block my prayers,
they block God.
I regain consciousness in short intervals,
each time closer to the ground.
I lie down in front of the sofa,
I crawl to the bathroom.
I regain consciousness of my frustration
lying, kissing the floor.
I regain the sense of pain
vomiting blood.
Schwag or placebo?
It doesn’t matter; I somatize the trip.
[ZPLPLPLYK], [ZPLPLPLYK].
Screeching chants, deep sobs,
untempered moans,
chains being dragged.
A compound beat
composed of wide nuances
of strong emotions.
I cast my gaze into the hallway
as I crawl through the frame
and call out to Frank.
A cry that stifles searching for him
in the growing distance.
When he manages to see me,
already in infinity,
He can’t contain the laughter.
My whimpering never reached his ears,
only the pathetic image
of a pretentious one who got lost
in his own thoughts.
Image he shares with the muses,
who cover their delicate little mouths
to hide depraved laughter.
Morbidly, they observe
the most embarrassing spectacle:
An "artist"
crawling on the floor,
all to find a bit of inspiration.
What did I get?
[ZPLPLPLYK], [ZPLPLPLYK].
Harmonies, melodies,
rhythms I don’t understand...
Words I’m not able to write,
a bad trip I don’t want to repeat
and the fear that everything
might have been a product
of my own mind.""",
        "cover_url": poemas_para_mi_cover,
        "pages": 3,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 40,
        "name": "miketta",
        "title": "Miketta",
        "dedication": None,
        "body": """You are the first artist
I have caressed
with indecency,
scratches
from my
frustrated guitarsit
"magical" hands.

And even though
you bled,
your nobility
impressed me:
you felt no pain,
you felt shame.

Shame for two fingers
stained with blood,
for your bite
on my arm.
Shame
for
displaying your desires
in a natural way.

Shame that I see
and makes me feel guilty.

You are the innocence
and kindness
that I need
to corrupt.

I desire to untie the knots
that keep your mind
bound to clichés.

Introducing you to my muses:
reality,
insomnia, sadness
and depression.

Inviting them to
inspire your artwork,
our future
story:
the only letter
of heartbreak
I’m interested in reading.

I detai you
with thoroughness
to understand
the reason behind
your tears.

I observe you
in detail
to know what
you want to hear.

I tell you that I am
a complete gentleman
while methodically
running my fingertips
over your back.

I figured out how
to caress your tattoo;
and you,
that I truly
intend
to harm you.""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 41,
        "name": "manipulation",
        "title": "Manipulation",
        "dedication": None,
        "body": """Yesterday, I bit your nipple
and I think I poisoned your chest.

Apparently, it was deep
and reached your lungs,
because today you walk
breathing with difficulty,
as if agonizing.

You scrutinize me erratically
with a
dull gaze,
seeking explanations
for my actions.

Hoping to find
my kindness.

It saddens me
to see you lament
the inexorable dissatisfaction
of your search.

You won’t find anything good
in me,
only diminish your faith.

But I understand you.
After all,
from venom
comes the antidote.

—With new traumas—.
What void are you trying to fill?""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 42,
        "name": "unforgettable",
        "title": "Unforgettable",
        "dedication": "Lounová",
        "body": """Unbelievable,
four years
and you remain
a recurring thought.

A fleeting scent
that I hold in my lungs.

The constant acidity
burning my palate.

An incessant implosion
reverberating in my chest.

The void
that I don’t feel ready to fill.

I try to do it
reconstructing you with words,
but inevitably
I fall onto common ground,
bursting hard
against reality:

That you’re not here,
that I need you,
and that, even though you’re the perfect muse,
I’m not enough for you.

Because I haven’t managed
to combine the perfect words
to immortalize your beauty.

Because I haven’t managed
to bring you down from the Parnassus.
To display you before the unbelieving
and insensitive.

Perhaps,
that’s why I may not deserve to have you;
or perhaps
I haven’t exerted
enough effort.

I haven’t dedicated my life
to immortalize yours,
writing the perfect poem.

Nor have my fingers pressed
with enough force
the keyboard until they bleed.

If I haven’t risked my life
to reach where you are,

how could I be such a hypocrite
to then tell you
that I would die for you?""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 43,
        "name": "grandmother",
        "title": "Grandmother",
        "dedication": None,
        "body": """I feel a bit hypocritical
receiving the
"heartfelt condolences."

I was never attached to her
and honestly
I don’t feel bad
for her death.

In fact, I feel tranquil
because her agony is over.

That’s why,
they should approach with a
"I am sorry that she suffered
in her final moments."

That is true consolation,
I could believe it is
a sincere comment.

Because empathy
comes from understanding others’ pain,

and even though I didn’t love her,
I feel sadness
because I saw her suffer.

Hopeless
with a tear
she made us understand
that she suffered when accepting her death.

At least in it
she found liberation
and there is no more suffering,

or well
only remains
that of the living
mourning her death.""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "poem_id": 44,
        "name": "balcony",
        "title": "Balcony",
        "dedication": None,
        "body": """If you feel like jumping, call me
and we’ll both jump.

So you’ll see that I’m not lying,
when I tell you:
"love is a decision";

that, if you give me your hand,
I would hold onto it for the rest of my life,

and accepting death,
is not so difficult,
if I have you by my side.
15""",
        "cover_url": poemas_para_mi_cover,
        "ig_url": "",
        "language_id": 2,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]


book_content = [
    {"content_id": 1, "book_id": 1},
    {"content_id": 2, "book_id": 1},
    {"content_id": 3, "book_id": 1},
    {"content_id": 4, "book_id": 1},
    {"content_id": 5, "book_id": 1},
    {"content_id": 6, "book_id": 1},
    {"content_id": 7, "book_id": 1},
    {"content_id": 8, "book_id": 1},
    {"content_id": 9, "book_id": 1},
    {"content_id": 10, "book_id": 1},
    {"content_id": 11, "book_id": 1},
    {"content_id": 12, "book_id": 1},
    {"content_id": 13, "book_id": 1},
    {"content_id": 14, "book_id": 1},
    {"content_id": 15, "book_id": 1},
    {"content_id": 16, "book_id": 1},
    {"content_id": 17, "book_id": 1},
    {"content_id": 18, "book_id": 1},
    {"content_id": 1, "book_id": 4},
    {"content_id": 2, "book_id": 4},
    {"content_id": 3, "book_id": 4},
    {"content_id": 4, "book_id": 4},
    {"content_id": 5, "book_id": 4},
    {"content_id": 6, "book_id": 4},
    {"content_id": 7, "book_id": 4},
    {"content_id": 8, "book_id": 4},
    {"content_id": 9, "book_id": 4},
    {"content_id": 10, "book_id": 4},
    {"content_id": 11, "book_id": 4},
    {"content_id": 12, "book_id": 4},
    {"content_id": 13, "book_id": 4},
    {"content_id": 14, "book_id": 4},
    {"content_id": 15, "book_id": 4},
    {"content_id": 16, "book_id": 4},
    {"content_id": 17, "book_id": 4},
    {"content_id": 18, "book_id": 4},
    {"content_id": 19, "book_id": 2},
    {"content_id": 20, "book_id": 2},
    {"content_id": 21, "book_id": 2},
    {"content_id": 22, "book_id": 2},
    {"content_id": 23, "book_id": 2},
    {"content_id": 24, "book_id": 2},
    {"content_id": 25, "book_id": 2},
    {"content_id": 26, "book_id": 2},
    {"content_id": 27, "book_id": 2},
    {"content_id": 28, "book_id": 2},
    {"content_id": 29, "book_id": 2},
    {"content_id": 30, "book_id": 2},
    {"content_id": 31, "book_id": 2},
    {"content_id": 32, "book_id": 2},
    {"content_id": 33, "book_id": 2},
    {"content_id": 34, "book_id": 2},
    {"content_id": 35, "book_id": 2},
    {"content_id": 19, "book_id": 5},
    {"content_id": 20, "book_id": 5},
    {"content_id": 21, "book_id": 5},
    {"content_id": 22, "book_id": 5},
    {"content_id": 23, "book_id": 5},
    {"content_id": 24, "book_id": 5},
    {"content_id": 25, "book_id": 5},
    {"content_id": 26, "book_id": 5},
    {"content_id": 27, "book_id": 5},
    {"content_id": 28, "book_id": 5},
    {"content_id": 29, "book_id": 5},
    {"content_id": 30, "book_id": 5},
    {"content_id": 31, "book_id": 5},
    {"content_id": 32, "book_id": 5},
    {"content_id": 33, "book_id": 5},
    {"content_id": 34, "book_id": 5},
    {"content_id": 35, "book_id": 5},
    {"content_id": 36, "book_id": 3},
    {"content_id": 37, "book_id": 3},
    {"content_id": 38, "book_id": 3},
    {"content_id": 39, "book_id": 3},
    {"content_id": 40, "book_id": 3},
    {"content_id": 41, "book_id": 3},
    {"content_id": 42, "book_id": 3},
    {"content_id": 43, "book_id": 3},
    {"content_id": 36, "book_id": 6},
    {"content_id": 37, "book_id": 6},
    {"content_id": 38, "book_id": 6},
    {"content_id": 39, "book_id": 6},
    {"content_id": 40, "book_id": 6},
    {"content_id": 41, "book_id": 6},
    {"content_id": 42, "book_id": 6},
    {"content_id": 43, "book_id": 6},
    {"content_id": 44, "book_id": 6},
    {"content_id": 45, "book_id": 4},
    {"content_id": 46, "book_id": 4},
    {"content_id": 47, "book_id": 4},
    {"content_id": 48, "book_id": 4},
    {"content_id": 49, "book_id": 4},
    {"content_id": 50, "book_id": 4},
    {"content_id": 51, "book_id": 4},
    {"content_id": 52, "book_id": 4},
    {"content_id": 53, "book_id": 4},
    {"content_id": 54, "book_id": 4},
    {"content_id": 55, "book_id": 4},
    {"content_id": 56, "book_id": 4},
    {"content_id": 57, "book_id": 4},
    {"content_id": 58, "book_id": 4},
    {"content_id": 59, "book_id": 4},
    {"content_id": 60, "book_id": 4},
    {"content_id": 61, "book_id": 4},
    {"content_id": 62, "book_id": 4},
    {"content_id": 63, "book_id": 5},
    {"content_id": 64, "book_id": 5},
    {"content_id": 65, "book_id": 5},
    {"content_id": 66, "book_id": 5},
    {"content_id": 67, "book_id": 5},
    {"content_id": 68, "book_id": 5},
    {"content_id": 69, "book_id": 5},
    {"content_id": 70, "book_id": 5},
    {"content_id": 71, "book_id": 5},
    {"content_id": 72, "book_id": 5},
    {"content_id": 73, "book_id": 5},
    {"content_id": 74, "book_id": 5},
    {"content_id": 75, "book_id": 5},
    {"content_id": 76, "book_id": 5},
    {"content_id": 77, "book_id": 5},
    {"content_id": 78, "book_id": 5},
    {"content_id": 79, "book_id": 5},
    {"content_id": 80, "book_id": 6},
    {"content_id": 81, "book_id": 6},
    {"content_id": 82, "book_id": 6},
    {"content_id": 83, "book_id": 6},
    {"content_id": 84, "book_id": 6},
    {"content_id": 85, "book_id": 6},
    {"content_id": 86, "book_id": 6},
    {"content_id": 87, "book_id": 6},
    {"content_id": 88, "book_id": 6},
]

language = [
    {"id": 1, "name": "spanish", "original_name": "español"},
    {"id": 2, "name": "english", "original_name": "english"},
]


book = [
    {
        "name": "libro_ii",
        "title": "Libro II",
        "pdf_url": libro_ii_pdf,
        "cover_url": libro_ii_cover,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "libro_i",
        "title": "Libro I",
        "pdf_url": libro_i_pdf,
        "cover_url": libro_i_cover,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "poemas_para_mi",
        "title": "Poemas para mí",
        "pdf_url": poemas_para_mi_pdf,
        "cover_url": poemas_para_mi_cover,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "libro_ii__book_ii",
        "title": "Libro II | Book II",
        "pdf_url": libro_ii__book_ii_pdf,
        "cover_url": libro_ii_cover,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "libro_i__book_i",
        "title": "Libro I | Book I",
        "pdf_url": libro_i__book_i_pdf,
        "cover_url": libro_i_cover,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "poemas_para_mi_poems_for_me",
        "title": "Poemas para mí | Poems for me",
        "pdf_url": poemas_para_mi__poems_for_me_pdf,
        "cover_url": poemas_para_mi_cover,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

poems_libro_ii = [
    {
        "name": "dios",
        "title": "Dios",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "identidad",
        "title": "Identidad",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "spica",
        "title": "Spica",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "moral",
        "title": "Moral",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "exhortacion",
        "title": "Exhortación",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "voz_de_escritor",
        "title": "Voz de Escritor",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "derrotismo",
        "title": "Derrotismo",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "utopia_de_ratas",
        "title": "Utopía de Ratas",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "reflexion_II",
        "title": "Reflexión II",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "reflexion_III",
        "title": "Reflexión III",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "reflexion_IV",
        "title": "Reflexión IV",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "reflexion_XII",
        "title": "Reflexión XII",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "no_es_suficiente",
        "title": "No es Suficiente",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "checa",
        "title": "Checa",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "odio",
        "title": "Odio",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "ella",
        "title": "Ella",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "media_de_lucky_rojo",
        "title": "Media de Lucky Rojo",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "reflexion_IX",
        "title": "Reflexión IX",
        "cover_url": libro_ii_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

poems_libro_i = [
    {
        "name": "nostalgia",
        "title": "Nostalgia",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "un_mundo_triste",
        "title": "Un Mundo Triste",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "acrilico",
        "title": "Acrílico",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "cliche",
        "title": "Cliché",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "cliche_II",
        "title": "Cliché II",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "dientes",
        "title": "Dientes",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "monotonia",
        "title": "Monotonía",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "stitch",
        "title": "Stitch",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "cansancio",
        "title": "Cansancio",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "otra_forma_de_dolor",
        "title": "Otra Forma de Dolor",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "caribe",
        "title": "Caribe",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "inspiracion",
        "title": "Inspiración",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "marea_baja",
        "title": "Marea Baja",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "la_casa_de_las_goteras",
        "title": "La Casa de las Goteras",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "femme_fatale",
        "title": "Femme Fatale",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "die_rosenrot",
        "title": "Die Rosenrot",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "reflexion_X",
        "title": "Reflexión X",
        "cover_url": libro_i_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

poems_poemas_para_mi = [
    {
        "name": "entre_dientes",
        "title": "Entre Dientes",
        "cover_url": poemas_para_mi_cover,
        "is_active": False,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "lounova",
        "title": "Lounová",
        "cover_url": poemas_para_mi_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "novia",
        "title": "Novia",
        "cover_url": poemas_para_mi_cover,
        "is_active": False,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "zplplplyk",
        "title": "[ZPLPLPLYK]",
        "cover_url": poemas_para_mi_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "miketta",
        "title": "Miketta",
        "cover_url": poemas_para_mi_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "manipulacion",
        "title": "Manipulación",
        "cover_url": poemas_para_mi_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "insuperable",
        "title": "Insuperable",
        "cover_url": poemas_para_mi_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "abuela",
        "title": "Abuela",
        "cover_url": poemas_para_mi_cover,
        "is_active": True,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "name": "balcon",
        "title": "Balcón",
        "cover_url": poemas_para_mi_cover,
        "is_active": False,
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

content_image_book_ii = [
    {
        "content_id": 1,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'dios.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 2,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'identidad.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 3,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'spica.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 4,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'moral.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 5,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'exhortacion.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 6,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'voz_de_escritor.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 7,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'derrotismo.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 8,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'utopia_de_ratas_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 8,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'utopia_de_ratas_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 9,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'reflexion_ii.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 10,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'reflexion_iii.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 11,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'reflexion_iv.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 12,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'reflexion_xii.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 13,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'no_es_suficiente.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 14,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'checa.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 15,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'odio.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 16,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'ella.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 17,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'media_de_lucky_rojo.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 18,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'reflexion_ix.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]
content_image_book_i = [
    {
        "content_id": 19,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'nostalgia.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 20,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'un_mundo_triste.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 21,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'acrilico.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 22,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'cliche.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 23,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'cliche_ii.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 24,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'dientes_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 24,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'dientes_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 25,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'monotonia_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 25,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'monotonia_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 26,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'stitch.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 27,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'cansancio_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 27,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'cansancio_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 28,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'otra_forma_de_dolor_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 28,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'otra_forma_de_dolor_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 29,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'caribe_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 29,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'caribe_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 29,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'caribe_p3.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 30,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'inspiracion_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 30,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'inspiracion_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 31,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'marea_baja_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 31,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'marea_baja_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 32,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'la_casa_de_las_goteras_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 32,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'la_casa_de_las_goteras_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 32,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'la_casa_de_las_goteras_p3.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 33,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'femme_fatale.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 34,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'die_rosenrot_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 34,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'die_rosenrot_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 35,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'reflexion_x.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]

content_image_poemas_para_mi = [
    {
        "content_id": 36,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'entre_dientes.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 37,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'lounova_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 37,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'lounova_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 38,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'novia.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 39,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'zplplplyk_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 39,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'zplplplyk_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 39,
        "pages": 3,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'zplplplyk_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 40,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'miketta_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 40,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'miketta_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 41,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'manipulacion.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 42,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'insuperable_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 42,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'insuperable_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 43,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'abuela_p1.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 43,
        "pages": 2,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'abuela_p2.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
    {
        "content_id": 44,
        "pages": 1,
        "img_url": f"{azure_blob_poem.replace('<blob_name>', 'balcon.jpg')}",
        "created_at": datetime.datetime.now(),
        "updated_at": datetime.datetime.now(),
    },
]
poem = poems_libro_ii + poems_libro_i + poems_poemas_para_mi
content = (
    content_book_ii
    + content_book_i
    + content_poemas_para_mi
    + content_book_ii_eng
    + content_book_i_eng
    + content_poemas_para_mi_eng
)
content_image = (
    content_image_book_ii + content_image_poemas_para_mi + content_image_book_i
)
